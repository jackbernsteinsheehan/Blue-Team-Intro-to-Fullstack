
# _____________________________________ Module 3 _____________________________________ #

import mysql.connector

class Connection:
    def __init__(self) -> None:
        
        self.host = 'localhost'
        # TODO: Read module_3.md instructions to set these up according to what you put
        self.user = 'root'
        self.password = 'Jj090809080908$'
        self.database = 'OSC'  ## Is this correct??
        
        self.status = 'inactive'
        self.conn = self.__init_conn()
        self.cursor = self.__init_conn()

    # ___________________ Connection Methods ___________________ #
    
    def __init_conn(self):
        if getattr(self, "conn", None) is not None:
            return self.conn.cursor(dictionary=True)

        try:
            connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            self.status = 'active'
            return connection
        
        except mysql.connector.Error as error:
            self.status = 'inactive'
            print(f"There was an error when attempting the connection with host {self.host}\n Error: {error}")
            return None
    
    def __init_cursor(self):

        if self.conn:
            return self.conn.cursor()
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
                count INT
            )
            """
            
            self.cursor.execute(query)
            
            self.conn.commit()
            
            return 'success'
            
        except mysql.connector.Error:
            
            return 'failure'
    
    def query_submit(self, table: str, data: dict) -> int:
        '''
        Arguably the most important function. This could go perfect or it can cause lots of issues.
        Enters a record on a table.
        Returns a standard status code according to the operation's outcome. Example, 201 if success.
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
        
        HINT:
        You don't know what type of data to expect! 
        What could you do to upload dynamic data? (e.g. **kwargs, dictionary, etc.. (?))
        '''
        if not isinstance(table, str) or not isinstance(data, dict) or len(data) == 0:
            return 400  # bad request

        try:
            cols = []
            placeholders = []
            values = []

            # Prepare data
            for col, val in data.items():
                cols.append(col)
                placeholders.append('%s')
                values.append(val)
            
            # Build query
            sql = "INSERT INTO " + table + " (" + ", ".join(cols) + ") VALUES (" + ", ".join(placeholders) + ")"

            # Execute and commit
            self.cursor.execute(sql, values)
            self.conn.commit()
            
            return 201

        except ValueError:
            # invalid identifier format
            return 400

        except mysql.connector.Error as e:
            # Map common MySQL errors to useful status codes
            # https://dev.mysql.com/doc/mysql-errors/8.0/en/server-error-reference.html
            if e.errno == 1146:       # ER_NO_SUCH_TABLE
                return 404
            elif e.errno == 1062:     # ER_DUP_ENTRY
                return 409
            elif e.errno in (1452,):  # ER_NO_REFERENCED_ROW_2 (FK fail)
                return 422
            else:
                # print(f"query_submit error [{e.errno}]: {e.msg}")
                return 500


    def query_extract(self, table: str, field: str, conditions: str) -> dict:
        '''
        Extract a record from a table. Allow for OPTIONAL filtering conditions. conditions should
        be passed as a boolean statement acceptable for SQL.
        '''
        
        query = '''
        SELECT {field}
        FROM {table}
        WHERE {str}
        '''

    
    def get_table_data(self) -> dict:
        '''
        Returns ALL of the information contained in a table.
        '''
        pass # TODO
        
    def show_tables(self) -> list[str]:
        '''
        Returns a list of all table names in the data base
        '''
        try:
            # Not sure if this query is correct
            query = '''
            SELECT table_name
            FROM information.schema.tables
            WHERE table_schema = DATABASE()
            AND table_type = 'BASE_TABLE'
            ORDER BY table_name
            '''
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            names = []
            for row in rows:
                names.append(row["table_name"])
            return names

        except mysql.connector.Error as error:
            print(f'show tables error: {error}')
            return []
    
    # __________________ Custom Query __________________ #
    
    def custom_query(self, query:str):
        '''
        Creates a custom query for potential user use.
        '''
        pass # TODO
    
    # ___________________ Danger Zone ___________________ #
    
    def query_delete_table(self):
        '''
        Deletes a specified table. Again, allow for OPTIONAL filtering conditions. 
        '''
        pass # TODO

    def query_delete_database(self):
        
        # TODO
        
        ... # Logic Here #
        
        user_input = input(f"Are you certain you want to delete {self.database} database? (Y/N)") # PLACEHOLDER layer of security
        
        if user_input == '':
            pass
        elif '':
            pass
        ...