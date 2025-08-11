
This file is where we will **bring it all together**.  

Up until now, you have:  
- Learned how to fetch and process stock/crypto data from public APIs.  
- Built a database connection layer to store/query records. 
- Built queries for SQL. 

Here, we are creating a **Commander** class that inherits from our `Connection` class in Module 3, giving it full access to our SQL methods. Commander will:  
- Fetch fresh stock and crypto data.  
- Initialize tables in our database.  
- Populate them with the processed data.  
- Provide basic CRUD operations for later use in API endpoints.  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  

**vvvv Do this vvvv**

1) Open **root** / backend / database / *Connection.py* (Module 3) and confirm that:  
   - `query_create_table` works for both `stocks` and `crypto`.  
   - `query_submit` accepts a **dict** for row data.  
   - `show_tables` correctly lists tables in your database.  

You’ll be calling these directly from Commander.

2) Open **root** / backend / *Commander.py*
In the `__init__` method, you’ll see we are **hardcoding some attributes** for now:  
```python
self.stock_parameters = ''   # replace with your API params
self.crypto_ticker = ''      # e.g., 'BTC'
self.crypto_limit = None     # optional limit for crypto data
```
Fill these with realistic values so your loaders have something to fetch. Perhaps its best to pass them as parameters to the class (?).

3) Implement the `__init_stocks_table` and `__init_crypto_table` methods. Read the context, understand the code and finalize the initialization of the tables according to out data.

Reminder of our structure:

```py
{
    "<ticker>": {
        "open": {"mean": ..., "std": ..., "median": ..., "low": ..., "max": ...},
        "high": {...},
        ...
    },
    "count": int,
    "standing": str
}
```

4) Commander will also handle basic database operations:

enter_record(table: str) —> insert a single record manually.
extract_record(table: str, key: dict) —> get a specific record by condition or filter.
delete_record(table: str, key: str) —> Delete a record by a unique key or filter.
extract_table(table: str) —> Return all records from a given table.

This step is the bridge for further simplifying the methods that you created in the Connection class onto our Commander methods.

## Further Notes ##

- This module is not meant to be fully automated yet. The idea is to get familiar with orchestrating multiple moving parts — API fetching, SQL storage, and CRUD operations — in one place.

- Don’t overcomplicate things. Get it working with minimal branching logic first.

- You can always refactor after you see it running. Test test test.

**This is arguably the most complicated module you will work on.** So please bring any questions you may have to our discussions.