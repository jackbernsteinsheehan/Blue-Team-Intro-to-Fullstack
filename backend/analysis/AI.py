
# _____________________________________ Module 5 _____________________________________ #

# Here we will connect with an OpenAI through its SDK. This will allow us to directly access a 
# functionality that ChatGPT would directly do.

from openai import OpenAI, AuthenticationError # pip install openai
from backend.utils.support import get_secret

class AI:
    
    def __init__(self) -> None:
        
        self.key = get_secret("OPENAI_KEY")
        self.client = self.__set_client()

    def __set_client(self):
        try:
            return # TODO: we are accessing the client via OpenAI SDK
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
            # TODO: Use our client to access a response given the prompt.
            # validate response using our method
            content = ...
            return {"message": "success", "response" : content}
        
        except AuthenticationError:
            return {"message":"API key is incorrect. Authentication is invalid", "response":{}}
        except Exception:
            return {"message":"There was an error initializing the prompt.", "response":{}}

        
        
    
            
        
    
    