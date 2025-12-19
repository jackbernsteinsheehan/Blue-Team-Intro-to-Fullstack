
# _____________________________________ Module 3 _____________________________________ #
## Remember to only commit this file to Git. Your changes to fetch_stocks 
## won't be compatible with Adriana's.
from numbers import Number
import mysql.connector
import logging
from dotenv import load_dotenv
import os

load_dotenv()

class Connection:
    def __init__(self) -> None:
        
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = 'OSC'
        
        self.status = 'inactive'
        self.conn = self.__init_conn()
        if not self.conn:
            raise RuntimeError("DB connect failed")
        self.cursor = self.conn.cursor(dictionary=True)

    # ___________________ Connection Methods ___________________ #
    
    def __init_conn(self):
        try:
            connection = mysql.connector.connect(
            user=self.user,
            password=self.password,
            database=self.database,
            unix_socket="/tmp/mysql.sock",
            )
            self.status = "active"
            return connection
        
        except mysql.connector.Error as error:
            self.status = 'inactive'
            print(f"There was an error when attempting the connection with host {self.host}\n Error: {error}")
            return None
    
    def __init_cursor(self):

        if self.conn:
            return self.conn.cursor(dictionary=True)
        else:
            raise AttributeError("Connection Error: `self.conn` Attribute does pose a valid data type.")
    
    # ___________________ Queries ___________________ #
    
    def query_create_table(self, name): # Here is a demo of a query to create a table
        try:
            # Here is the pre-defined structure of a table
            query = f"""
            CREATE TABLE {name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ticker VARCHAR(5),
                metric VARCHAR(10),
                mean DOUBLE,
                median DOUBLE,
                std DOUBLE,
                low DOUBLE,
                max DOUBLE,
                count INT,
                standing VARCHAR(20)
            );
            """
            
            self.cursor.execute(query)
            tables = self.show_tables()
            self.conn.commit()
            
            return f'success. Tables are: {tables}'
            
        except mysql.connector.Error as error:
            
            return error
        from numbers import Number

    def query_submit(self, table: str, payload: dict[dict[str, dict[str, float]]]) -> int:
        """

        This method has been tested. It works. It accepts data formatted as outlined in Module 1 and returns a status code.

        Arguably the most important function. This could go perfect or it can cause lots of issues.
        Enters a record on a table.
        Returns a standard status code according to the operation's outcome. Example, 201 if success.
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
        
        HINT:
        You don't know what type of data to expect! 
        What could you do to upload dynamic data? (e.g. **kwargs, dictionary, etc.. (?))
    
        Accepts data in this format:
        {
        "IBM": {
            "open": {"mean": float, "std": float, "median": float, "low": float, "max": float},
            "high": {...}, "low": {...}, "close": {...}, "volume": {...}
        },
        "count": int,
        "standing": str
        }
        Inserts rows into columns:
        (ticker, metric, mean, median, std, low, max, count, standing)
        """

        # Make sure it's a dict
        if not isinstance(payload, dict):
            raise ValueError("payload must be a dict")

        count_val = payload["count"]
        standing_val = payload["standing"]

        if not isinstance(count_val, Number):
            raise ValueError("payload['count'] must be numeric")
        if not isinstance(standing_val, str):
            raise ValueError("payload['standing'] must be a string")

        # Flatten data
        rows = []
        metrics_expected = ("open", "high", "low", "close", "volume")

        for ticker, metrics in payload.items():
            if ticker in ("count", "standing"):
                continue
            if not isinstance(metrics, dict):
                raise ValueError(f"payload['{ticker}'] must be a dict of metrics")
            for metric_name, stats in metrics.items():
                if metric_name not in metrics_expected:
                    continue  # or raise if you want strict checking
                if not isinstance(stats, dict):
                    raise ValueError(f"payload['{ticker}']['{metric_name}'] must be a dict")

                # pull stats (all required; error if missing or wrong type)
                try:
                    mean_v = stats["mean"]
                    std_v = stats["std"]
                    median_v = stats["median"]
                    low_v = stats["low"]
                    max_v = stats["max"]
                except KeyError as e:
                    raise ValueError(f"Missing stat {e} under {ticker}/{metric_name}")

                # Check types
                for key, val in (("mean",mean_v),("std",std_v),("median",median_v),("low",low_v),("max",max_v)):
                    if not isinstance(val, Number):
                        raise ValueError(f"Stat '{key}' for {ticker}/{metric_name} must be numeric")

                rows.append((ticker, metric_name, mean_v, median_v, std_v, low_v, max_v, count_val, standing_val))

        if not rows:
            return 0

        # Build query
        sql = f"""INSERT INTO {table}
                (ticker, metric, mean, median, std, low, max, count, standing)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        # Execute query
        with self.conn.cursor() as cur:
            cur.executemany(sql, rows)
        self.conn.commit()

        return 201

    
    def query_extract(self, table: str, field: str, conditions: str=None) -> list[dict[str, str]]:
        '''
        
        This method has been tested. It works. Returns data like this:
        [{'ticker': 'IBM', 'mean': 5.5}, {'ticker': 'IBM', 'mean': 5.5}, {'ticker': 'HEY', 'mean': 8.7}]

        Extract a record from a table. Allow for OPTIONAL filtering conditions. conditions should
        be passed as a boolean statement acceptable for SQL.
        -table: the table name
        -field: comma-separated columns
        '''
        try:
            # Handle comma-separated vals
            field = field.strip()
            if field == '' or field == '*':
                fields_sql = '*'
            else:
                parts = field.split(',')
                quoted = []
                for p in parts:
                    name = p.strip()
                    quoted.append(f'`{name}`')
                fields_sql = ', '.join(quoted)

            # Table
            table_sql = f'`{table}`'

            # Optional filtering conditions
            where_sql = ''
            if isinstance(conditions, str) and conditions.strip():
                # Add splitting for mutliple conditions?
                conditions = conditions.strip()
                if conditions:
                    where_sql = " WHERE " + conditions
            
            # Build query
            sql = f"SELECT {fields_sql} FROM {table_sql}{where_sql}"

            # Execute query
            #print(sql)
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()

            # make a list
            result = []
            for row in rows:
                result.append(row)
            
            #print(result)
            return result

        except(TypeError, ValueError) as error:
            print(f'query_extract input error: {error}')
            return []
        except mysql.connector.Error as error:
            print(f"query_extract DB error [{getattr(error,'errno','?')}]: {getattr(error,'msg', str(error))}")
            return []

    
    def get_table_data(self, table: str) -> list[dict[str, int]]:
        '''
        This method has been tested. It works. Still need to decide how we want the data to be formatted.

        Returns ALL of the information contained in a table. Return data looks like this: 

        [{'id': 1, 'ticker': 'IBM', 'metric': 'open', 'mean': 5.5, 'median': 5.5, 'std': 5.5, 
        'low': 5.5, 'max': 5.5, 'count': 3, 'standing': 'good'}, 
        {'id': 2, 'ticker': 'IBM', 'metric': 'high', 'mean': 5.5, 'median': 5.5, 'std': 5.5, 
        'low': 5.5, 'max': 5.5, 'count': 3, 'standing': 'good'}
        '''
        try:
            sql = f'SELECT * FROM {table}'
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()

            # How do we want the data?
            '''
            for row in rows:
                row_id = row['id']
                ticker = row['ticker']
                metric = row['metric']
                mean = row['mean']
                median = row['median']
                std = row['std']
                low = row['low']
                maximum = row['maximum']
                count = row['count']
                standing = row['standing']
            '''
            return rows
        except Exception as e:
            return e

    def show_tables(self) -> list[str]:
        '''
        Returns a list of all table names in the data base
        '''
        try:
            # Not sure if this query is correct
            query = '''
            SELECT TABLE_NAME AS name
            FROM information_schema.TABLES
            WHERE TABLE_SCHEMA = DATABASE()
              AND TABLE_TYPE = 'BASE TABLE'
            ORDER BY TABLE_NAME;
            '''

            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            names = []
            for row in rows:
                names.append(row["name"])
            return names

        except mysql.connector.Error as error:
            print(f'show tables error: {error}')
            return []
    
    # __________________ Custom Query __________________ #
    
    def custom_query(self, query:str):
        '''
        Creates a custom query for potential user use.
        Talk to frontend to see what else they could want
        '''
        pass
    
    # ___________________ Danger Zone ___________________ #
    
    def query_delete_table(self, table, conditions=None):
        '''
        This method has been tested. It works.

        Deletes a specified table. Again, allow for OPTIONAL filtering conditions. 
        '''
        try:
            if isinstance(conditions, str):
                sql = f'DROP TABLE `{table}` WHERE {conditions};'
                self.cursor.execute(sql)
                self.conn.commit()
                new_table_list = self.show_tables()
                return f'Table deleted: {table}. Current tables are: {new_table_list}.'

            if not isinstance(conditions, str):
                sql = f'DROP TABLE `{table}`;'
                self.cursor.execute(sql)
                self.conn.commit()
                new_table_list = self.show_tables()
                return f'Table deleted: {table}. Current tables are: {new_table_list}.'

        except mysql.connector.Error as error:
                    return f'DB error: {error}'
        except Exception as error:
            return f'There was an error: {error}'


    def query_delete_database(self):
        
        # TODO
        
        ... # Logic Here #
        
        user_input = input(f"Are you certain you want to delete {self.database} database? (Y/N)") # PLACEHOLDER layer of security
        
        if user_input == '':
            pass
        elif '':
            pass
        ...