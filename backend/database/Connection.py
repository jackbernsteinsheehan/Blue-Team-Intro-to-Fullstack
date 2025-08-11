
# _____________________________________ Module 3 _____________________________________ #

import mysql.connector
# pip install mysql-connector-python

class Connection:
    def __init__(self) -> None:
        
        self.host = 'localhost'
        # TODO: Read module_3.md instructions to set these up according to what you put
        self.user = ''
        self.password = ''
        self.database = ''
        
        self.status = 'inactive'
        self.conn = self.__init_conn()
        self.cursor = self.__init_conn()

    # ___________________ Connection Methods ___________________ #
    
    def __init_conn(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
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
    
    def query_submit(self) -> int:
        '''
        Arguably the most important function. This could go perfect or it can cause lots of issues.
        Enters a record on a table.
        Returns a standard status code according to the operation's outcome. Example, 201 if success.
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status
        
        HINT:
        You don't know what type of data to expect! 
        What could you do to upload dynamic data? (e.g. **kwargs, dictionary, etc.. (?))
        '''
        pass # TODO

    def query_extract(self) -> dict:
        '''
        Extract a record from a table. Allow for OPTIONAL filtering conditions.
        '''
        pass # TODO
    
    def get_table_data(self) -> dict:
        '''
        Returns ALL of the information contained in a table.
        '''
        pass # TODO
        
    def show_tables(self) -> list:
        '''
        Returns a list of all table names in the data base
        '''
        pass # TODO
    
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
    
