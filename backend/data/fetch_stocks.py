import requests
import pandas as pd
from pprint import pprint

API_KEY = "K7C6AKO9TCQAU4E1"  # your Alpha Vantage key


def get_data_details(data: dict, days: int = 7) -> dict:
    """
    Take the raw AlphaVantage JSON response and compute summary stats
    for the most recent `days` entries (default: 7).

    Returns a dict like:
    {
        "symbol": "IBM",
        "open":   {"mean": ..., "std": ..., "median": ..., "low": ..., "max": ...},
        "high":   {...},
        "low":    {...},
        "close":  {...},
        "volume": {...},
        "count":  int,   # number of days actually used (<= days)
    }
    """
    try:
        # Find the time series block (e.g. "Time Series (Daily)")
        time_series_key = next((key for key in data.keys() if "Time Series" in key), None)
        if not time_series_key:
            raise ValueError("No time series data found in response.")
        
        time_series_data = data[time_series_key]

        # Sort dates newest → oldest and take the most recent `days` entries
        all_dates = sorted(time_series_data.keys(), reverse=True)
        recent_dates = all_dates[:days]

        records = []
        for date in recent_dates:
            stats = time_series_data[date]
            records.append({
                "open":   float(stats["1. open"]),
                "high":   float(stats["2. high"]),
                "low":    float(stats["3. low"]),
                "close":  float(stats["4. close"]),
                "volume": float(stats["5. volume"]),
            })

        if not records:
            raise ValueError("No recent records found in time series data.")

        df = pd.DataFrame(records)

        stats_dict: dict[str, dict[str, float]] = {}
        for col in df.columns:
            stats_dict[col] = {
                "mean":   float(round(df[col].mean(),   2)),
                "std":    float(round(df[col].std(),    2)),
                "median": float(round(df[col].median(), 2)),
                "low":    float(round(df[col].min(),    2)),
                "max":    float(round(df[col].max(),    2)),
            }

        result = {
            "symbol": data["Meta Data"].get("2. Symbol", "Unknown"),
            "open":   stats_dict["open"],
            "high":   stats_dict["high"],
            "low":    stats_dict["low"],
            "close":  stats_dict["close"],
            "volume": stats_dict["volume"],
            "count":  len(df),   # how many days we actually summarized (<= days)
        }

        return result
    except Exception as error:
        print(f"Error parsing stock data details: {error}")
        return {}


def get_standing(details: dict) -> str:
    """
    Classify the stock based on the recent-week stats.
    """
    try:
        open_stats = details['open']
        high_stats = details['high']
        low_stats = details['low']
        close_stats = details['close']

        price_range = high_stats["mean"] - low_stats["mean"]
        volatility = close_stats['std']
        skew = close_stats['median'] - close_stats['mean']

        if price_range > 10 and volatility > 5:
            standing = "risky"
        elif skew > 2:
            standing = "improving"
        elif skew < -2:
            standing = "declining"
        else:
            standing = "stable"

        return standing
    except Exception as e:
        print(f"Error determining standing: {e}")
        return "unknown"


def fetch_stock_data(
    symbol: str,
    base_url: str = "https://www.alphavantage.co",
    endpoint: str = "query",
    days: int = 7,
) -> dict | None:
    """
    Fetch the most recent `days` (default: 7) of daily data for `symbol`
    and return:

    {
        "IBM": {
            "open":   {...},
            "high":   {...},
            "low":    {...},
            "close":  {...},
            "volume": {...}
        },
        "count": int,        # number of days in the summary (<= days)
        "standing": str,
    }
    """
    try:
        # Build the URL and params for AlphaVantage (TIME_SERIES_DAILY)
        request_uri = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        params = {
            "function": "TIME_SERIES_DAILY",  # daily data, most recent 100 points by default :contentReference[oaicite:1]{index=1}
            "symbol": symbol,
            "apikey": API_KEY,
            "outputsize": "compact",         # latest ~100 days; we only use the last `days`
        }

        response = requests.get(request_uri, params=params)

        if response.status_code == 404:
            raise Exception("404 Not Found – check the request URL and parameters.")
        elif response.status_code == 403:
            raise Exception("403 Forbidden – check your API key / permissions.")
        elif response.status_code != 200:
            raise Exception(f"Unexpected status code: {response.status_code}")

        print('Yay! The connection works!\n')

        data = response.json()

        # Handle AlphaVantage error formats explicitly
        if "Note" in data:
            raise Exception(f"AlphaVantage note / rate limit: {data['Note']}")
        if "Error Message" in data:
            raise Exception(f"AlphaVantage error: {data['Error Message']}")

        details = get_data_details(data, days=days)
        if not details:
            return None

        standing = get_standing(details)
        symbol_key = details.get("symbol", symbol)

        metrics = ["open", "high", "low", "close", "volume"]
        symbol_block = {metric: details[metric] for metric in metrics if metric in details}

        result = {
            symbol_key: symbol_block,
            "count": details.get("count", 0),
            "standing": standing,
        }

        return result

    except Exception as some_error:
        print(f"There was an issue with the data fetching function. Error:\n{some_error}")
        return None


if __name__ == "__main__":
    # Most recent week (7 daily candles)
    result = fetch_stock_data("IBM", days=7)
    pprint(result)
