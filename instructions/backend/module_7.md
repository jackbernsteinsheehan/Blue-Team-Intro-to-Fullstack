
## Final Disclaimer

*If you do not wish to initialize an AWS account due to the payment system that AWS requires you are not obliged to do so*. The scope of the project has been completed, and this project will not fully be launched to production as most of the architecture we created is not meant be used that way.

If you do not wish to continue, then congratulations, you have successfully completed the backend side of the project!

# AWS App Runner

By now you should:

- Have a separate repo of your backend code
- Created and tested that APIs work locally
- Deleted all print statements
- Have seen or been through the App Hosting demo by Daniel

...

Recall our secret gathering function `get_secret` that gathers values from our LOCAL .env file. On production this function won't work. We will instead store our values inside of `AWS Secrete Manager`, and have our program connect with these values on a production environment. We will access these values via AWS SDK (boto3).

## Instructions to AWS IAM HERE ##

Open the file where the `get_secret` function is located. And override the content with the following code:

```py
import boto3 # pip install boto3
import os
import json
import logging as log
from dotenv import load_dotenv
from typing import List

log.basicConfig(level=log.INFO)


LOCAL_ENV_PATH = '' # <--- Your local path to .env here

class GetSecretWrapper:
    def __init__(self, secretsmanager_client):
        self.client = secretsmanager_client

    def get_secret(self, arn):
        try:
            
            response = self.client.get_secret_value(SecretId=arn)
            
            return response["SecretString"]
        except self.client.exceptions.ResourceNotFoundException:
            log.warning(f"The requested secret {arn} was not found.")
            return None
        except Exception as error:
            log.error(f"Error fetching secret: {error}.")
            raise

def get_secret(secret_key):
    """
    Retrieves the value for a specific key from the AWS secret
    whose ARN is stored in a environment variable.

    Falls back to a local .env file if secret fetching fails.
    """
    try:
        secret_arn = os.environ.get("IAM_ARN") # IMPORTANT: ARN given saved on .env

        client = boto3.client("secretsmanager") # starts the client
        wrapper = GetSecretWrapper(client)
        secret_string = wrapper.get_secret(secret_arn) # gets a string of JSON representation of secrets

        if not secret_string:
            raise Exception("Secret content is empty or missing")
        
        secret_dict:dict = json.loads(secret_string) # parses to standard JSON

        # Looks up the input variable name
        if secret_key not in secret_dict: 
            raise KeyError(f"Key '{secret_key}' not found in secret.")

        return secret_dict[secret_key]

    # if it happens that something fails, it likely means that we are testing secrete retrieval
    # locally. In which case we  simply fall back to our old system using local .env
    except Exception as e:
        # Development loading
        load_dotenv(LOCAL_ENV_PATH)
        return os.environ.get(secret_key)
```
Read the comments to understand how the code works.