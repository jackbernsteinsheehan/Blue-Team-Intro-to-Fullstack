from Connection import Connection

db = Connection()
'''
result = db.query_submit("nude_table", {
    "HEY": { # HEY as an example
        "open": {
            "mean": 8.7,
            "std": 5.4,
            "median": 5.8,
            "low": 9.7,
            "max": 5.6
        },
        "high": {
            "mean": 100,
            "std": 6.7,
            "median": 40.5,
            "low": 100,
            "max": 75
        },
        "low": {
            "mean": 87,
            "std": 5,
            "median": 5.7,
            "low": 10.5,
            "max": 89 
        },
        "close": {
            "mean": 4.5,
            "std": 65,
            "median": 6.5,
            "low": 10.5,
            "max": 11.5 
        },
        "volume": {
            "mean": 5.1,
            "std": 31.5,
            "median": 20.5,
            "low": 7,
            "max": 8
        }
    },
    "count": 4,
    "standing": "bad"  # added after using the get_standing() function
})
'''

#result = db.query_extract('test_metrics', "ticker, mean", "metric = 'open' AND mean > 0 AND mean < 10")
#result = db.show_tables()
#result = db.query_delete_table('example_tablee')
result = db.get_table_data('test_metrics')
#result = db.query_create_table("example_tablee")
print(result)
