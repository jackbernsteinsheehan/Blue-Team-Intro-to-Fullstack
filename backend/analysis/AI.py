
# _____________________________________ Module 5 _____________________________________ #

# Here we will connect with an OpenAI through its API. This will allow us to directly access a functionality that ChatGPT 
# would directly do.

# We will intrdouce something called a .env.local which allows us to keep hidden variables within our own machine and load up
# to any place we want in source code

# create a .env.local file at the root
# if you have it already, skip this
    # locate the .gitignore file and type in the name of the file anywhere
    # .env.local
    # make sure the name of the file turns gray whenever we save with this change.
    
# .gitignore will NOT push the selected files to the repository. That's the whole point

from openai import OpenAI, AuthenticationError # pip install openai
from backend.utils.support import get_secret

class AI:
    
    def __init__(self) -> None:
        
        self.key = get_secret("OPENAI_KEY")
        self.client = self.__set_client()

    def __set_client(self):
        try:
            return OpenAI(self.key) # we are accessing the client via OpenAI SDK
        except Exception as error:
            print(f"Error ocurred when intializing the client. Error: {error}")
    
    def __is_valid_response(self, response):
        if not response:
            print("No response to check")
            return
        
        status = response["message"]
        if status == "success":
            return True
        return False
    
    def request_query(self, prompt):
        
        if not self.client:
            return {"message": "There was an error getting OpenAI client started", "response": {}}
        if not prompt:
            return {"message": "Prompt set is invalid", "response":{}}
        try:
            response = self.client.chat.completions.create(
                ... # TODO
            )
            # validate response using our method
            return {"message": "success", "response" : response}
        
        except AuthenticationError:
            return {"message":"API key is incorrect. Authentication is invalid", "response":{}}
        except Exception:
            return {"message":"There was an error initializing the prompt.", "response":{}}

        
        
    
            
        
    
    