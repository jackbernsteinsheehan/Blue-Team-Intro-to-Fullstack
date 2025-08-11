
# _____________________________________ Module 4 _____________________________________ #

# Pay close attention to the absolute import pathing.
# We don't do relative paths for projects like these.

# ____________________ Loaders ____________________ #
from backend.data.fetch_stocks import fetch_stock_data
from backend.data.fetch_crypto import fetch_crypto_data

# connection to SQL class that we created in Module 3
from backend.database.Connection import Connection

# main commander class. Similar to a main function.
# we will use this export to manage all of the API endpoint we will create
class Commander(Connection):
    
    def __init__(self) -> None:
        super().__init__()
        
# ____________________ Stocks ____________________#

        # vvv Hardcode This Attributes vvv #
        
        self.stock_parameters = ''
        
        self.stock_data:dict = self.__load_stocks()

# _____________________ Crypto _____________________#

        # vvv Hardcode These Attributes vvv #
        
        self.crypto_ticker = ''
        self.crypto_limit = None
        
        self.crypto_data:dict = self.__load_crypto()
        
# __________________________________________________ #

        self.tables:list = self.show_tables() 
        
    def __load_stocks(self):
        result = fetch_stock_data(self.stock_parameters)
        return result
    
    def __load_crypto(self):
        result = fetch_crypto_data(self.crypto_ticker, self.crypto_limit) if self.crypto_limit else  fetch_crypto_data(self.crypto_ticker)
        return result
    
# __________________________________________________ #

    def __init_stocks_table(self):
        '''
        Initializes and populates the stocks table from self.stock_data
        ''' 
        for ticker, metrics in self.stock_data.items():
            if ticker in ['count', 'standing']:
                continue

            for metric, stats in metrics.items():
                status = self.query_submit(
                    ...
                )
                
                if status != 201:
                    pass # something happens

    def __init_crypto_table(self):
        '''
        Initializes and populates the crypto table from self.crypto_data
        '''
        for ticker, metrics in self.crypto_data.items():
            if ticker in ['count', 'standing']:
                continue

            for metric, stats in metrics.items():
                status = self.query_submit(
                    ...
                )
                
                if status != 201:
                    pass # something happens
    
    def __init_tables(self):
        '''
        *This function should only be run once*
        
        This function will populate the tables for both of our data sets within the same data base.
        Of course, one will be for the stock description and the other for the cyrpto.
        
        We must check if there are tables that already exist. At the start, there shouldn't.
        We will check by using the `show_tables` method from our child class.
        
        We then must create a table using the `query_create_table` function.
        
        We will iterate over the dictionaries within the `self.stock_data` and `self.crypto_data`, and populate 
        the entries one by one with the `query_submit` function. 
        '''
        try:
            self.query_create_table('stocks')
            self.query_create_table('crypto')
            
            self.__init_stocks_table()
            self.__init_crypto_table()
 
        except Exception as error:
            print("There was an error initializing the tables operation")
            return None
    
    # _________________ CRUD _________________ # TODO
    
    def enter_record(self, table:str):
        pass
    
    def extract_record(self, table:str, key:dict):

        if not self.__is_valid_table(table):
            return # idk some error here, or whatever. You are the engineer.
        
        record = self.query_extract(key)
        
        return record
    
    def delete_record(self, table:str, key:str):
        
        return 'yayy!! Deleted' or 'oops! There was an issue' # maybe think of status codes (?)
    
    def extract_table(self, table:str):
        pass
    
    # ________________ Support ________________ #

    def __is_valid_table(self, table):
        return table in self.tables