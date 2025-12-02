
# _____________________________________ Module 1 _____________________________________ #

import requests # run `pip install requests` if haven't already
import pandas as pd 
import json
from pprint import pprint

# For code running (print testing, etc...), run the file as a `module` with the flag -m
# py -m backend.data.fetch_stocks <- no .py
def get_data_details(data:dict)->dict:
    """
    stocks = pd.DataFrame(data)
    stocks.columns = ['open', 'high', 'low', 'close', 'volume']
    count = 0

    print(stocks.columns())
    print(stocks.mean())
    print(stocks.std())
    print(stocks.median())
    print(stocks.min())
    print(stocks.max())
    """
    try:
        """
        if "Meta Data" not in data:
            raise ValueError("No 'Meta Data' found in API response")
        
        meta = data["Meta Data"]
        details = {
            "symbol": meta.get("2. Symbol", "Unknown"),
            "last_refreshed": meta.get("3. Last Refreshed", "Unknown"),
            "interval": meta.get("4. Interval","N/A"),
        }
        """
        timeSeriesKey = next((key for key in data.keys() if "Time Series" in key), None)
        if not timeSeriesKey:
            raise ValueError("No tie series data found in response.")
        
        timeSeriesData = data[timeSeriesKey]

        #mostRecentDate = sorted(timeSeriesData.keys())[-1]
        #latestData = timeSeriesData[mostRecentDate]

        """
        details["latest"] = {
            "data": mostRecentDate,
            "open": latestData.get("1. open", "N/A"),
            "high": latestData.get("2. high", "N/A"),
            "low": latestData.get("3.low", "N/A"),
            "close": latestData.get("4. close", "N/A"),
            "volume": latestData.get("5. volume", "N/A"),
        }
        """
        records = []
        for date, stats in timeSeriesData.items():
            records.append({
                "open": float(stats["1. open"]),
                "high": float(stats["2. high"]),
                "low": float(stats["3. low"]),
                "close": float(stats["4. close"]),
                "volume": float(stats["5. volume"])
            })   

        df = pd.DataFrame(records)

        stats_dict = {}
        for col in df.columns:
            stats_dict[col] = {
                "mean": float(round(df[col].mean(), 2)),
                "std": float(round(df[col].std(), 2)),
                "median": float(round(df[col].median(), 2)),
                "low": float(round(df[col].min(), 2)),
                "max": float(round(df[col].max(), 2))
            }

        result = {
            "symbol": data["Meta Data"].get("2. Symbol", "Unknown"),
            "open": stats_dict["open"],
            "high": stats_dict["high"],
            "low": stats_dict["low"],
            "close": stats_dict["close"],
            "volume": stats_dict["volume"],
            "count":len(df)
        }

        return result
    except Exception as error:
        print(f"Error parsing stock data details: {error}")
        return {}

# we will export this function 
def fetch_stock_data(params:dict, base_url:str=" https://www.alphavantage.co", endpoint:str="query"):
    '''
    URL Sample:
    https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&outputsize=full&apikey=demo
    
    API Key:
    K7C6AKO9TCQAU4E1
    
    Full Documentation:
    
    https://www.alphavantage.co/documentation/ <---------- # TODO 1
    
    '''
    
    # TODO 2: build the request URI here!! use the parameters (base_url, endpoint, params) as building blocks
    #request_uri = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    try:
        # creates the request
        request_uri = f"{base_url}/{endpoint}"
        response = requests.get(request_uri, params=params) 

        
        # 404 not found
        if response.status_code == 404: 
            raise Exception("The error indicates that the request was not found. Check the request and try again.")
        # 403 forbidden
        elif response.status_code == 403: 
            raise Exception("Access was denied to you. Ensure exact API key spelling and try again. If issue persists contact Daniel")
        # 200 OK
        elif response.status_code == 200: 
            print('Yay! The connection works!\n')

        # get the content of the API. This should include the JSON files
        data = response.json() 
        pprint(data)
            
        # TODO 4: Uncomment and implement
        details = get_data_details(data)
        if details:
            details["standing"] = get_standing(details)
            return details

        # TODO 5
        #standing = get_standing(details)
        #result = details["standing"] = standing
        
        # return result # Done

    except Exception as some_error:
        print(f"There was an issue with the data fetching function. Error:\n{some_error}")
        return None

# TODO 3: Test the function!
#fetch_stock_data('', '', '') 

# TODO 4


# TODO 5
def get_standing(details:dict)->str:
    try:
        open_stats = details['open']
        high_stats = details['high']
        low_stats = details['low']
        close_stats = details['close']

        price_range = high_stats["mean"] - low_stats["mean"]
        volatility = close_stats['std']
        skew = close_stats['median'] - close_stats['mean']

        if price_range >10 and volatility>5:
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
    # pass

if __name__ == "__main__":
    params = {
        "function": "TIME_SERIES_MONTHLY",
        "symbol": "IBM",
        "apikey": "K7C6AKO9TCQAU4E1"
    }
    result = fetch_stock_data(params)
    pprint(result)
