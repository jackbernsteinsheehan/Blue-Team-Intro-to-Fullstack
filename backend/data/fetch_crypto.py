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

    #Quary parameterssent to the API
    params = {
        'fsym': symbol, #from symbol crypto ticker (ex: BTC)
        'tsym': 'USD', #convert to USD
        'limit': days  #number of days to fetch
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

        #Parse JSON data from API response
        data = response.json()

        #validate the structure of the incoming JSON
        if not data or "Data" not in data or "Data" not in data["Data"]:
            raise ValueError("Crypto API returned invalid data structure")

    except Exception as e:
        #print error and stop
        print(f"Failed to fetch crypto data: {e}")
        return None

    # Parse OHLCV records
    parsed_records = []
    # Iterate through each record and extract relevant data
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

    #loop through each column to calculate statistics
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
        symbol: stats, #statistics grouped under the crypto symbol
        "count": len(df) #number of records fetched
    }

    # Determine standing
    # Reuse the get_standing function from fetch_stocks module
    standing = get_standing(details)
    details["standing"] = standing

    return details


# test and print on terminal that it works
if __name__ == "__main__":
    result = fetch_crypto_data(symbol="BTC", days=30)
    pprint(result)
