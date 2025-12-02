import logging
import os
import sys
from flask_cors import CORS
from flask import Flask, jsonify


try:
    from backend.database.Connection import Connection
except ModuleNotFoundError:
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
    from backend.database.Connection import Connection

def create_app(): 
    app = Flask(__name__)
    CORS(app)
    setup_logging(app)
    return app

def setup_logging(app):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )
    app.logger.info("Logging is configured.")

# Initialize app
app = create_app()

@app.route('/create_table/<table>')
def create_table(table):
    status = Connection.query_create_table(table)
    return status

# ________________ General Endpoints _________________#

# one route when conditions are omitted
@app.route('/extract/<table>/<field>/data', defaults={'conditions': None})
# one route when conditions are supplied (note: path converter allows spaces/slashes once URL-encoded)
@app.route('/extract/<table>/<field>/<path:conditions>/data')
def extract_data(table, field, conditions=None):
    '''
    This method has been tested. It works. Returns data like this:
    [{'ticker': 'IBM', 'mean': 5.5}, {'ticker': 'IBM', 'mean': 5.5}, {'ticker': 'HEY', 'mean': 8.7}]

    Extract a record from a table. Allow for OPTIONAL filtering conditions. Conditions should
    be passed as a boolean statement acceptable for SQL.
    -table: the table name
    -field: comma-separated columns

    Example call: query_extract('test_metrics', "ticker, mean", "metric = 'open' AND mean > 0 AND mean < 10")
    Notice how the boolean conditions are formatted. Use this exact format when hitting this endpoint.
    '''
    db = Connection()
    try:
        if conditions:
            data = db.query_extract(table, field, conditions)
        else:
            data = db.query_extract(table, field)
    except Exception as e:
        # This will log the *real* error in your Flask terminal
        app.logger.exception("Error in extract_data")
        # And return the message to curl so you can see it
        return {"error": str(e)}, 500

    # data is likely a list[dict], so jsonify it
    return jsonify(data), 200

@app.route('/get/<table>/data')
def get_table_data(table):
    '''
    This method has been tested. It works.

    Returns ALL of the information contained in a table. Return data looks like this: 

    [{'id': 1, 'ticker': 'IBM', 'metric': 'open', 'mean': 5.5, 'median': 5.5, 'std': 5.5, 
    'low': 5.5, 'max': 5.5, 'count': 3, 'standing': 'good'}, 
    {'id': 2, 'ticker': 'IBM', 'metric': 'high', 'mean': 5.5, 'median': 5.5, 'std': 5.5, 
    'low': 5.5, 'max': 5.5, 'count': 3, 'standing': 'good'}
    '''
    db = Connection()
    data = db.get_table_data(table)
    return jsonify(data), 200

# _________________ Systematic Endpoint _________________ #

@app.route('/health') 
def health():
    '''
    You can also check for the status of the database, AI client, etc...
    This just checks the status of the app as a whole.
    '''
    return "Endpoint is healthy", 200

if __name__ == "__main__":
    app.run(host='localhost', port=5000)