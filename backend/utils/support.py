from dotenv import load_dotenv # pip install python-dotenv
from os import getenv

LOCAL_PATH_TO_SECRET = "Absolute/path/to/.env"

class MissingSecretError(Exception):
    pass

def get_secret(key:str):
    load_dotenv(LOCAL_PATH_TO_SECRET)
    value = getenv(key, None)
    
    if not value:
        raise MissingSecretError(f"Not found secrete value for key: {key} in environment.")
    return value