
For this module we will initialize our SQL Data Base connection. A data base is exactly like it sounds, it stores all sorts of data.
There are two types of data bases: 

**Relational DB**:
A structured, table-like, strict setting data bases like SQL, PostgreSQL, etc... The actual storage of data is within `tables` with a set number of columns with respective data types. This "structure" is otherwise known as the `schema` for this table.
**Non-Relational DB**:
Inserts JSON (dictionaries in Python) data structures. Very liberal and flexible. They are otherwise called NoSQL DBs. Instead of passing a specific `schema` as previously defined, we upload all sorts of keys/columns/parameters freely, called `records` onto a `collection` rather than a table.
The most popular Non-Relational DB and great choices include MongoDB, FirebaseDB, Redis and Cassandra.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

SQL stands for Structured Query Language

For this project, we will focus on SQL.
1) Download MySQL Workbench Here:

https://dev.mysql.com/downloads/workbench/

Follow the steps and download the appropriate version for your system.

2) Initialize the connection with your own machine.
For Mac/Linux run this one the terminal:
```bash
sudo /usr/local/mysql/support-files/mysql.server start`
```

For Windows:
```
Ctrl+Shift+Esc to open Task Manager
Open Services
Look for something along the lines of MySQL
Click start
```

You can also run:
```bash
net start MySQL
```

3) Open the MySQL Workbench application, and create a local connection (click the little plus symbol next to "MySQL Connections")

4) Fill out the needed parameters:

Connection Name: `localhost`
Username: [replace with whatever]
Password: Click `store in keychain` and select a password that you wont forget! Be very careful.
**If you forget this, there is a way to recover. Talk to me if this happens** 

5) Test Connection if everything went alright in step 2, then this should work no problem and you will receive some kind of success message.

6) Open the connection. You will be shown something similar to a big-old terminal. This is where all of the `queries` occur.

7) Now that you have a connection, you must start a data base. The query for it is the following:

CREATE DATABASE <the_db_name_without_the_signs>

8) Now open the following file:

**root** / backend / pipeline / Connection.py

A template is already set for you. This is a class with OOP practices. OOP is *greatly* used in enterprise organizations, and is of the most requested skill for jobs. Mastering it is a good idea.

9) Fill out the attributes with the information you used to initialize a local connection and the database.

10) Your task for this module will implement all of the methods that include CRUD operations (Create, Read, Update, Delete) as well as some additional core functionalities.
I set the example with the first method, `query_create_table`, which includes a query within it to accomplish a task. **Add as much guardian code as you can.** A good Software Engineer must think of how a user might interact with your program such that error may occur. If something does not behave as expected, the entire application may crash due to unhandled errors.

Supplementary information:

# Structure Definition Example

Looking ahead the tables will look something like this...
(Assuming the names are `Table 1` and `Table 2`. They won't...)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

### Table 1: Stock Metrics

| id | ticker | metric | mean | std  | median | min_val | max_val | count |
|----|--------|--------|------|------|--------|---------|---------|-------|
| 1  | IBM    | open   | 100  | 1.0  | 120    | 90      | 130     | 90    |
| 2  | IBM    | close  | 100  | 1.0  | 120    | 90      | 130     | 90    |
| 3  | IBM    | low    | 100  | 1.0  | 120    | 90      | 130     | 90    |
| 4  | IBM    | high   | 100  | 1.0  | 120    | 90      | 130     | 90    |
| 5  | MSFT   | open   | 100  | 1.0  | 120    | 90      | 130     | 108   |
| 6  | MSFT   | close  | 100  | 1.0  | 120    | 90      | 130     | 108   |
| 7  | MSFT   | low    | 100  | 1.0  | 120    | 90      | 130     | 108   |
| 8  | MSFT   | high   | 100  | 1.0  | 120    | 90      | 130     | 108   |
| 9  | AMZN   | open   | 100  | 1.0  | 120    | 90      | 130     | 321   |


### Table 2: Crypto Metrics

| id | ticker | metric | mean | std  | median | min_val | max_val | count |
|----|--------|--------|------|------|--------|---------|---------|-------|
| 1  | BTC    | open   | 100  | 1.0  | 120    | 90      | 130     | 90    |
| 2  | BTC    | close  | 100  | 1.0  | 120    | 90      | 130     | 90    |
| 3  | BTC    | low    | 100  | 1.0  | 120    | 90      | 130     | 90    |
| 4  | BTC    | high   | 100  | 1.0  | 120    | 90      | 130     | 90    |
| 5  | ETH    | open   | 100  | 1.0  | 120    | 90      | 130     | 108   |
| 6  | ETH    | close  | 100  | 1.0  | 120    | 90      | 130     | 108   |
| 7  | ETH    | low    | 100  | 1.0  | 120    | 90      | 130     | 108   |
| 8  | ETH    | high   | 100  | 1.0  | 120    | 90      | 130     | 108   |
                                      