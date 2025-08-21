
*This is the final step for backend programming.*

We have a lot of Python functions, but how do we make them useful? How can we use our functions do something outside of our local computer?

This is where APIs come in (Application Programming Interfaces). That allow use to send information across the internet via HTTP (Hypertext Transformation Protocol). Essentially, a client like your PC navigating Steam games will send a request to the host (Steam), to gather information about the games available to buy, gather information about new deals, etc...

We can create our own API that will communicate any type of data that we have fetched and analyze to our frontend host to ultimately display it on our platform.

Please attend the `Hosting Python Apps` presentation to get an live demo to the introduction to Python, WSGI, and AWS. If you happened to miss it or you are ahead ask Daniel for the slides.

# Your Task

You will create API endpoints for ALL functions that we have worked on so far. You can work under `backend/blueprints/` directory. Most of the functions are found in the `Commander.py` file, which are mostly logistical; but allow frontend to manage everything else. Make sure to also include your AI feature onto a separate blueprint file.
Remember to create as much guardian code as possible within the API endpoints. This is very important as we have to know **exactly** what went wrong should the API fail, the usage of the API happened to be incorrect or was used under unexpected context.

As seen on the demo, tie all of the blueprint files on the main file: `backend/run_app.py`. On this file paste the following code:

```py
import logging
from flask_cors import CORS
from flask import Flask

def create_app(): 
    
    ... # TODO Setup Here

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

app = create_app()

# _________________ Systematic Endpoint _________________ #

@app.route('/health') # ALWAYS great to have. 
def health():
    '''
    You can also check for the status of the database, AI client, etc...
    This just checks the status of the app as a whole.
    '''
    return "OK", 200

if __name__ == "__main__":
    app.run(...)
```

Print statements across your app will most likely crash your application when used in production. So you have two options: 1) delete all of the print statements, or 2) use logging instead (recommended).

If you decide to use logging, make sure to only log critical information. It is also great for debugging; feel free to log anything at all if needed, but remember to delete before sending to production.

For any file you want to log on, then do this at the top of your file:
```py
import logging as log
logger = log.getLogger(__name__) # FOR LOGGING TESTING
```
and do something like:
```py
log.info("The client for our database has been started!")
log.warn("For development environment use only!")
log.error("There was an error gathering API data from ___.")
```

*To test your APIs you can use your web browser for only `GET` requests, but I strongly recommend learning the industry standard Postman.* Remember to initialize the listener via WSGI or if your on Windows simply run the `run_app.py` file that also starts the local listener to your API. 

We are now ready to split the repository into frontend and backend before starting with AWS.
Find a way to grab the entire `backend/` directory, rename it to something descriptive, and create a new GitHub repository with all of the code. Keep the repo private and give access to your teammates and admins.
Make sure to fix any module importing changes, and fix any issues with the migration.