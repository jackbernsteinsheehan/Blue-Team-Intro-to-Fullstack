
# _____________________________________ Module 1 _____________________________________ #

import requests
import pandas as pd 
import json
from pprint import pprint

# For code running (print testing, etc...), run the file as a `module` with the flag -m
# py -m backend.data.fetch_stocks <- no .py
def get_data_details(data:dict)->dict:
    
    try:
        if "Meta Data" not in data:
            raise ValueError("No 'Meta Data' found in API response")
        
        symbol = data["Meta Data"].get("2. Symbol", "Unknown")
        
        timeSeriesKey = next((key for key in data.keys() if "Time Series" in key), None)
        if not timeSeriesKey:
            raise ValueError("No tie series data found in response.")
        
        timeSeriesData = data[timeSeriesKey]
        
        stocks = pd.DataFrame.from_dict(timeSeriesData, orient='index')
        stocks = stocks.rename(columns = {
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. volume": "volumn",
        })
        stocks = stocks.astype(float)

        stats = {}
        for col in stocks.columns:
            stats[col] = {
                "mean": stocks[col].mean(),
                "std": stocks[col].std(),
                "median": stocks[col].median(),
                "low": stocks[col].min(),
                "high": stocks[col].max(),
            }
        
        count = len(stocks)

        result = {
            symbol: stats,
            "count": count
        }

        pprint(result)

        return result
    
    except Exception as error:
        print(f"Error parsing stock data details: {error}")
        return {}

# TODO 5
def get_standing(details:dict)->str:
    try:
        symbol = next(key for key in details.keys() if key != "count")

        data = details[symbol]

        open_stats = data["open"]
        close_stats = data["close"]
        high_stats = data["high"]
        low_stats = data["low"]

        price_range = high_stats["mean"] - low_stats["mean"]
        volatility = close_stats["std"]
        skew = close_stats["median"] - close_stats["mean"]

        if price_range > 10 and volatility >5:
            standing = "Risky"
        elif skew > 2:
            standing = "Improving"
        elif skew < -2:
            standing = "Declining"
        else:
            standing = "Stable"

        pprint(f"Determined standing: {standing}")

        return standing
    
    except Exception as error:
        print(f"Error calculating standing: {error}")
        return "Unknown"
    
# we will export this function 
def fetch_stock_data(params:str, base_url:str=" https://www.alphavantage.co", endpoint:str="query"):
    '''
    URL Sample:
    https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&outputsize=full&apikey=demo
    
    API Key:
    VDYLR2S1C4ZWII9J
    
    Full Documentation:
    
    https://www.alphavantage.co/documentation/ <---------- # TODO 1
    
    '''
    result = {}
    
    # TODO 2: build the request URI here!! use the parameters (base_url, endpoint, params) as building blocks
    request_uri = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
    try:
        # creates the request
        response = requests.get(request_uri) 
        
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
            data:dict = response.json() 
            pprint(data)
            
            # TODO 4: Uncomment and implement
            details = get_data_details(data)

            # TODO 5
            standing = get_standing(details)
            result = details["standing"] = standing
        
        return result # Done

    except Exception as some_error:
        print(f"There was an issue with the data fetching function. Error:\n{some_error}")
        return None

# TODO 3: Test the function!
fetch_stock_data('', '', '') 

# TODO 4


# TODO 5
def get_standing(details:dict)->str:
    try:
        symbol = next(key for key in details.keys() if key != "count")

        data = details[symbol]

        open_stats = data["open"]
        close_stats = data["close"]
        high_stats = data["high"]
        low_stats = data["low"]

        price_range = high_stats["mean"] - low_stats["mean"]
        volatility = close_stats["std"]
        skew = close_stats["median"] - close_stats["mean"]

        if price_range > 10 and volatility >5:
            standing = "Risky"
        elif skew > 2:
            standing = "Improving"
        elif skew < -2:
            standing = "Declining"
        else:
            standing = "Stable"

        return standing
    
    except Exception as error:
        print(f"Error calculating standing: {error}")
        return "Unknown"
