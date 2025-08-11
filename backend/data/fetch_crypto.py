
# _____________________________________ Module 2 _____________________________________ #

import requests
from pprint import pprint

def fetch_crypto_data(symbol, days=30):
    '''
    Sample:
    https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=30

    Full Documentation:
    
    https://developers.coindesk.com/documentation/legacy/Price/SingleSymbolPriceEndpoint
    
    Key:
    
    ---
    
    
    ADD ENOUGH ERROR HANDLING (try-except, if None checks, etc...)!
    
    '''
    url = 'https://min-api.cryptocompare.com/data/v2/histoday'
    
    key = ''
    
    params = {
        'fsym': symbol,
        'tsym': 'usd',
        'limit': days  # number of days
    }
    headers = {
        'authorization': f'Apikey {key}'
    }
    
    response = requests.get(url, params=params, headers=headers)
    status_code = response.status_code
    
    # TODO: Status Code Validation
    # if eveything is in order, uncomment:
    # data = response.json()
    
    # parsed_data = parse_data()
    
    return result


def parse_data(data:dict):
    pass