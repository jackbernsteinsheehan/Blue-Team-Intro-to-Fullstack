
# _____________________________________ Module 1 _____________________________________ #

import requests # run `pip install requests` if haven't already
from pprint import pprint

# For code running (print testing, etc...), run the file as a `module` with the flag -m
# py -m backend.data.fetch_stocks <- no .py

# we will export this function 
def fetch_stock_data(params:str, base_url:str=" https://www.alphavantage.co", endpoint:str="query"):
    '''
    URL Sample:
    https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&outputsize=full&apikey=demo
    
    API Key:
    ---
    
    Full Documentation:
    
    https://www.alphavantage.co/documentation/ <---------- # TODO 1
    
    '''
    result = {}
    request_uri = f'' # TODO 2: build the request URI here!! use the parameters (base_url, endpoint, params) as building blocks
    try:
        
        response = requests.get(request_uri) # creates the request
        
        if response.status_code == 404: # 404 not found
            raise Exception("The error indicates that the request was not found. Check the request and try again.")
        elif response.status_code == 403: # 403 forbidden
            raise Exception("Access was denied to you. Ensure exact API key spelling and try again. If issue persists contact Daniel")
        elif response.status_code == 200: # 200 OK
            print('Yay! The connection works!\n')

            data:dict = response.json() # get the content of the API. This should include the JSON files
            pprint(data)
            
            # TODO 4: Uncomment and implement
            # details = get_data_details(data)
            
            # TODO 5
            # standing = get_standing(details)
            # result = details["standing"] = standing
        
        # return result # Done

    except Exception as some_error:
        print(f"There was an issue with the data fetching function. Error:\n{some_error}")
        return None

fetch_stock_data('', '', '') # TODO 3: Test the function!

# TODO 4
# def get_data_details(data:dict)->dict:
    # pass # Follow instructions carefully :)

# TODO 5
# def get_standing(details:dict)->str:
    # pass
