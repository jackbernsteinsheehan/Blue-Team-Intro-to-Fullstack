
# Backend start HERE! # 

Please read the overview file /README.md if you haven't yet

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

On your terminal do the following.

```bash
cd backend
py -m venv venv
```
Then for Mac/Linux:
```bash
source venv/bin/activate
```
For Windows:
```bash
venv\Scripts\activate.bat
```

This will activate a virtual environment to insert all of our dependencies and requirements via pip (python's package manager). Every time you want to download a python library, the package won't be stored in your OS permanently but within the venv directory instead that will work on your project. In the end, we will be able to pass all of our dependencies and libraries into a `requirements.txt` file. More on that later.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

This file is where we will *fetch* data from an API (application programming interface aka. some server-side function)

Eventually, you will create your own API to communicate data through HTTPS requests (hyper-text transformation protocol secure)

**Declaimer**: DO NOT follow every single instruction. This is your time to experiment and to learn on you own. If you thin there are better ways to complete a task, go for it.

This code is NOT tested. This is intentional because your job is to solve issues and debug. The intention of this project is not for it to feel like another school assignment. With time you will come to find out how different academics are from the modern software engineering discipline.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


Open the first file to implement found in **root** / backend / data / *fetch_stocks.py*

**Do not code yet! Look over step 1 and 2. Understand the underlying mechanism of API fetching**

1) Once in the file, the fist function you will need to implement is the `fetch_stock_data` function. The goal of this function is to gather the data we need via API. In most cases an API takes three different components: a. `base_url` - This is the request url from where the response is expected to come from. Its what tells the server that the information will be coming from there.
b. `endpoint` - the specific functionality that you are calling
c. `params` - any parameters included within the request. These are always necessary; as they function exactly the same way as a python function, where f(x) = y then the param is x and returns some value y.

2) The most important aspect of being a Software Engineer in my opinion is being able to learn for yourself. The docstring in the function includes an example request URI found in the documentation page. What you must do is figure out what parameters it takes, which ones you should worry about, and make your first request from there. Start by reading/skimming over some of the documentation.  If you have to, go find a YouTube video or ask ChatGPT on making a Python API request.

3) After understanding how to make a request, you can now implement the function. Build the request URI based on your knowledge. Depending on the response you get different things will happen. Try creating a request that will receive data from the *IBM* ticker/symbol, for *monthly* recurring data. The key is a given (also included in the docstring). Once you have built the request URI call the function. You should received a bunch of JSON data.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

4) Uncomment lines 41 & 56/57. Here you will implement the `get_data_details` function. Find a way to extract the *records*:
```python
[
{
    "1. open": "158.3200",
    "2. high": "165.0000",
    "3. low": "153.2100",
    "4. close": "158.8500",
    "5. volume": "69951563"
},
{
    ...
}
...

]
```
This being *one sample* of many, it represents a format called *OHLCV* data.
Extract all of its records into a list of record, get the *number of records* and store it, then do the following:
```python
import pandas as pd
stocks = pd.DataFrame(data)
stocks.columns = ['open', 'high', 'low', 'close', 'volume']
count = 0 # Number of records -> implement!
```
for each, find the columns, find the *mean*, *standard deviation*, the *median*, the *lowest* and the *maximum* using pandas.

Understand how to use pandas to find these attributes! Use Google, use Pandas documentation, use ChatGPT. Just learn!

You are working with the Pandas data analytics framework (Excel on steroids). You are essentially *parsing* and cleaning the original data into a new format that we want. In the end you can turn the *dataframe* from and to a python list of dictionaries by doing something like:

```python
my_final_data = dataframe_used.to_dict()
```

The goal for the `get_data_details` function is to return a JSON/dict with the following format:
```python
{
    "Ticker/Symbol (IBM in this case)": {
        "open": {
            "mean": int/float,
            "std": int/float,
            "median": int/float,
            "low": int/float,
            "max": int/float,
        },
        "high": {
            "mean": int/float,
            "std": int/float,
            "median": int/float,
            "low": int/float,
            "max": int/float,
        },
        "low": {
            "mean": int/float,
            "std": int/float,
            "median": int/float,
            "low": int/float,
            "max": int/float,
        },
        ...
    },
    "count": int
}
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

5) Uncomment lines 44/45 & 60/61. 

Implement the following logic onto the `get_standing` function:

```python
open_stats = data['open']
high_stats = data['high']
low_stats = data['low']
close_stats = data['close']

price_range = high_stats['mean'] - low_stats['mean']
volatility = close_stats['std']
skew = close_stats['median'] - close_stats['mean']

# You can tune these thresholds however you like
if price_range > 10 and volatility > 5:
    standing = "risky"
elif skew > 2:
    standing = "improving"
elif skew < -2:
    standing = "declining"
else:
    standing = "stable"

return standing
```

Understand this logic fully and paste it onto the function's body.

The final structure of the dictionary that the main export function will return looks like:

```python
{
    "IBM": { # IBM as an example
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
            "mean": float,
            "std": float,
            "median": float,
            "low": float,
            "max": float 
        },
        "close": {
            "mean": float,
            "std": float,
            "median": float,
            "low": float,
            "max": float 
        },
        "volume": {
            "mean": float,
            "std": float,
            "median": float,
            "low": float,
            "max": float 
        }
    },
    "count": int,
    "standing": str  # added after using the get_standing() function
}
```

If there are any issues, find a way to resolve them and get the expected output all the same. 
Good Luck!

***any questions reach out to me :)**

This was the first module to complete