
## Overview ##

The project will have one page with chart(s) of stock data, AI description of data, and AI implementations and solutions. The data gathered will be stored in an MySQL database.

Here is the planned architecture of the project:

For this project we will be using public APIs to request data to practice using request frameworks included in the Python runtime. We will be integrating OpenAI API calls, which will have various uses. And by incorporating a local MySQL database to store necessary data components we will store clean versions of the data gathered.

Python will be the sole backend language that will cover all operations as a whole. We will be using Flask for the app creation, and Gunicorn WSGI for the gateway of the backend APIs and finally, using AWS AppRunner will allow us to host our Flask APIs. 
The APIs will include:
- CRUD operation endpoints that will call database management for the seamless front-end use.
- Data analytic tools for metrics, tools and filters
- System health indicators

To implement UI/UX and mimic best user experience we will be using the industry standard React web framework for building web applications. Our main language here will be TypeScript that will bring forth tools like React & Tailwind CSS. This frontend will use the data from the backend APIs to display charts and tables, along with its respective prognostications via open-source frameworks with their respective documentations. 
Front-end's job will be to keep components clear, codebase readable, gather APIs efficiently, and make the page look nice, clean and professional.

**Note** *that core features and implementations will be for you and your team to decide.* 
Although guides and instructions are given, in the end we want to see what **you** can accomplish. Creativity plays a huge role on the success of the project. Make it yours.

There is a lot going on in this project. **This is okay!** Not even I know how 
to navigate most of these components. Not without some research first.

# Additional features:

Filters (by tickers, date range, volume, etc...)

Chat Visualization > predictions performed vs actual data. 

# Tech Stack

| Layer      | Technology                         |
|------------|------------------------------------|
| Frontend   | React + TypeScript + Tailwind CSS  |
| Backend    | Python, Flask, Gunicorn            |
| Hosting    | AWS App Runner (Flask)             |
| AI         | OpenAI API                         |
| Database   | SQL (Local -> AWS-hosted (?))      |
| APIs       | Public stock data sources          |

# Git / GitHub Basics #

If you happen to need a guide to the basic and most-common commands for git, here they are:

**Getting started (cloning repo)**

`git clone <url>`
Get the url from GitHub.
This will *clone* the repository. Which means that all of the files included within a workspace will
be transferred locally (to your machine). Now you can begin working.

**Pushing new changes**

`git add .`
"Hey git, I want to *stage* the changes I made in this directory for a future push"

`git commit -m "some message goes here!"`
"Hey git, remember those changes that I made and added? Yeah... I want them to be compiled in one bunch
and get ready to be pushed. Here is my -m message"

-m *flag* allows you to set a message for this commit preparation. Clearly explain what the changes are and what you did.

`git push`
"Hey git, I want to send these changes to my cloud GitHub repo. Send all the files!"

From here is just rinse and repeat every time you have made a significant change.
**note** that this can also be done with VS Code features itself, but I would recommend practicing with 
the git CLI first (command-line interface).
