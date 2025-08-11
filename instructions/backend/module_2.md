
Open the file...
**root** / backend / data / fetch_crypto.py

Your task will require you to complete the `fetch_crypto_data` function, that will gather historical crypto prices, along with its important information.

Previously we have observed the *OHLCV* data, and this time, we will work with a similar type of data.

As you may observe, most of the request has already been done for you. You have the following tasks:

1) Test the response. I have imported the pprint (pretty print) module that allows us to see a dictionary structure a lot more clearly within the integrated terminal.
2) Add status code error handling. Raise appropriate errors when needed with its respective reasoning.
3) You will need to parse the response to only extract the records into an array. In this case, it should look like this:

```python
[{
    'close': 82919.47, # 
    'conversionSymbol': '',
    'conversionType': 'direct',
    'high': 83608.26, # 
    'low': 76581.52, # 
    'open': 78561.62, #
    'time': 1741651200,
    'volumefrom': 46456.32, # 
    'volumeto': 3744822903.84 #
    },
    {
        ...
    },
    ...
]
```

From here we will only care about the same keys we previously worked on (the values with # right next to them).
Find a way to return a new structure with the requirements above. 
**Implement the function `parse_data` to achieve this goal**
This process is called *parsing*, the process of cleaning, converting and reading data.

4) As we have done before, since the two dictionary structures are the same as from module 1, we will now get the details to describe this crypto data. You may notice that we have already created a function for this, `get_data_details`, and `get_standing`. We can either use these again or repeat the code. (Optional) If you wish to use these again, create another file called `support.py`, and move the two functions here, to be used by the other two modules.

5) Our `fetch_crypto_data` should output an structurally-identical JSON as `fetch_stock_data`, as they use the same process. Both of these function will be exported to another module for future use.

6) Wherever there is the most *minimal potential* to be any kind of error, add some type of error handler. This can be...

```python

try:
    data = load_api_data(url) # This could fail!

except Exception as error:
    print(f"Oh no! An error ocurred. Error\n{error}")

```

or...

```python

data = load_api_data(url) # It technically works, but may return None

if not data:
    raise ValueError(f"There was a problem reading the data! Expected data type: {dict} but got {type(data)}")

```

Again, the final return product should pose the structure:

```python
{
    "BTC": { # Bitcoin as an example
        "open": {
            "mean": float,
            "std": float,
            "median": float,
            "low": float,
            "max": float
        },
        "high": {
            "mean": float,
            "std": float,
            "median": float,
            "low": float,
            "max": float
        },
        "low": {
            ... 
        },
        "close": {
            ... 
        },
        "volume": {
            ... 
        }
    },
    "count": int,
    "standing": str  # adding after using an external function to get the standing
}
```

Good luck!