
# _____________________________________ Module 1 _____________________________________ #

import requests # run `pip install requests` if haven't already
import pandas as pd 
import json
from pprint import pprint

# For code running (print testing, etc...), run the file as a `module` with the flag -m
# py -m backend.data.fetch_stocks <- no .py
def get_data_details(data:dict)->dict:
    
    try:
        if "Meta Data" not in data:
            raise ValueError("No 'Meta Data' found in API response")
        
        meta = data["Meta Data"]
        details = meta.get("2. Symbol", "Unknown")
            #"symbol": meta.get("2. Symbol", "Unknown"),
            #"last_refreshed": meta.get("3. Last Refreshed", "Unknown"),
            #"interval": meta.get("4. Interval","N/A"),
        #}
        timeSeriesKey = next((key for key in data.keys() if "Time Series" in key), None)
        if not timeSeriesKey:
            raise ValueError("No tie series data found in response.")
        
        timeSeriesData = data[timeSeriesKey]

        #mostRecentDate = sorted(timeSeriesData.keys())[-1]
        #latestData = timeSeriesData[mostRecentDate]
        
        stocks = pd.DataFrame.from_dict(timeSeriesData, orient='index', dtype=float)
        stocks.columns = ['open', 'high', 'low', 'close', 'volume']
        #stocks.index = pd.to_datetime(stocks.index)
        stocks = stocks.astype(float)

        for column in stocks.columns:
            stocks[column] = {
                "mean" : print(round(stocks[column].mean())),
                "standard deviation" : print(round(stocks[column].std())),
                "median" : print(round(stocks[column].median())),
                "min" : print(round(stocks[column].min())),
                "max" : print(round(stocks[column].max()))
            }

        #details["latest"] = {
            #"data": mostRecentDate,
            #"open": latestData.get("1. open", "N/A"),
            #"high": latestData.get("2. high", "N/A"),
            #"low": latestData.get("3.low", "N/A"),
            #"close": latestData.get("4. close", "N/A"),
            #"volume": latestData.get("5. volume", "N/A"),
        #}

        
        print("Details values: ", details, type(details))
        my_final_data = stocks.to_dict()

        return my_final_data
    except Exception as error:
        print(f"Error parsing stock data details: {error}")
        return {}

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
            # standing = get_standing(details)
            # result = details["standing"] = standing
        
        # return result # Done

    except Exception as some_error:
        print(f"There was an issue with the data fetching function. Error:\n{some_error}")
        return None

# TODO 3: Test the function!
fetch_stock_data('', '', '') 

# TODO 4


# TODO 5
# def get_standing(details:dict)->str:
    # pass
