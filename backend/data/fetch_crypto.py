# _____________________________________ Module 2 _____________________________________ #

import requests
import pandas as pd
from pprint import pprint
from fetch_stocks import get_standing  # reuse the get_standing function

def fetch_crypto_data(symbol: str, days: int = 30):
    """
    Fetch historical crypto prices for a given symbol.
    """
    url = 'https://min-api.cryptocompare.com/data/v2/histoday'
    key = ''  # Add your API key here if required

    params = {
        'fsym': symbol,
        'tsym': 'USD',
        'limit': days
    }

    headers = {
        'authorization': f'Apikey {key}'
    }

    # Fetch data from API
    try:
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 404:
            raise Exception("Request not found. Check the URL or parameters.")
        elif response.status_code == 403:
            raise Exception("Access denied. Check your API key or permissions.")
        elif response.status_code != 200:
            raise Exception(f"Unexpected status code: {response.status_code}")

        data = response.json()
        if not data or "Data" not in data or "Data" not in data["Data"]:
            raise ValueError("Crypto API returned invalid data structure")

    except Exception as e:
        print(f"Failed to fetch crypto data: {e}")
        return None

    # Parse OHLCV records
    parsed_records = []
    for record in data["Data"]["Data"]:
        parsed_records.append({
            "open": float(record["open"]),
            "high": float(record["high"]),
            "low": float(record["low"]),
            "close": float(record["close"]),
            "volume": float(record["volumeto"])  # using 'volumeto' as total traded value
        })

    # Convert to DataFrame for stats
    df = pd.DataFrame(parsed_records)
    stats = {}
    for col in df.columns:
        stats[col] = {
            "mean": df[col].mean(),
            "std": df[col].std(),
            "median": df[col].median(),
            "low": df[col].min(),
            "high": df[col].max()
        }

    # Build final details dictionary
    details = {
        symbol: stats,
        "count": len(df)
    }

    # Determine standing
    standing = get_standing(details)
    details["standing"] = standing

    return details


# --------------------- Test & pretty-print --------------------- #
if __name__ == "__main__":
    result = fetch_crypto_data(symbol="BTC", days=30)
    pprint(result)
