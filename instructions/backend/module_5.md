
# Set-up

The core functionality of our program is pretty much done. Now we will focus on incorporating AI into our own program. We will be using OpenAI's ChatGPT models to accomplish cool tasks that automate work that would've been very difficult to do 5 years ago.

We will introduce the `.env` file. One of the best Software Engineering practices that you **must** learn. Every time you use an API key, secrete variable value, or global value that you want to use across your app, you use this file to keep this information hidden from the public for security reasons.

Create the .env file inside of the backend directory. Just like any variable, it has its name and its value. If we want to connect to the OpenAI client to start using AI we will first need to use our paid API key to access it. To keep this key secret, we will create a variable inside .env
```bash
OPENAI_KEY="tobegiven"
```

If we decide to push our code onto GitHub, this file would still be visible to the public, which defeats the purpose of keeping our keys secret. So what we will do is *ignore this file from being shown on our repository* via the `.gitignore` file. You should have it under `backend/.gitignore`, but if you don't go ahead and create it.

On this file, type the path of the file you wish to ignore. If you wanted to make random test files (such as a test.py file for whatever) then it's always great to ignore them and keep any mess hidden.

I created a `get_secret` function that simply retrieves any given value, but since the .env file is local we will have ot modify the file to tell our system that we must look into a specific path of where the wished .env file is hidden (`backend/utils/support.py`). Navigate to this file and modify the `LOCAL_PATH_TO_SECRET` variable to specify the path to our .env file.

**Now, anywhere that we have used any API key or secret value, instead of hardcoding it into our code, we will do the same as before: add the name/value to .env then use the the get_secret function to retrieve the value.**

It would be a good idea to place your username, password, database values onto .env as well. 

# Programming

I already created most of the AI class for you. Please read over the code and understand how it works. I reiterate, it is essential to know how to use OOP as best as you can. Try to get comfortable with it.

You must implement the `TODO` blocks.
Test the AI usage once you have investigated how to use the client online.

It is time to give you lots of freedom and think what AI could do best for our application. Think in broad terms and have as most imagination as you possibly can. We have a bunch of data, would it be a good idea to give AI possibly hundreds of lines of data for it to analyze? Hint: No, since it ramps up API token usage, possible token limits, inaccuracy, etc... Start thinking like a Software Engineer. Problem solve and think of other possible pathways to solutions.

Create as many files as you want, create classes and functions, ask me (Daniel) questions if needed. Think of inputs and outputs before even beginning to code. Keep your directory structure organized. You are essentially building a platform feature from scratch.