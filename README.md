https://github.com/AJ-ANUJ/Fibonacci-Numbers-Generator/assets/26610301/449f63bb-bddb-4eed-966c-71ef7a600695


# Documentation

This web app for generating the first n Fibonacci numbers has been build by using Django framework for backend, relational database and React.js for frontend development.

This design decision is taken to maintain **separation of concerns**.

>**Note**: 0 is being considered as the first fibonacci number.

The directory structure is as follows:

.
├── README.md

├── cz-biohub-env

├── first_n_fib_nums

└── frontend_fib_nums

first_n_fib_nums directory contains the codebase for the backend of the web app.

frontend_fib_nums directory contains the codebase for the frontend of the web app.

# Design Details

## Backend Design

The backend server for this web app has the following:

1. A django model called FibonacciTable: This model is the relational database for the web app.

2. The FibonaciTable has the following schema

> a. Primary key column, Name: fib_no, data type: BigIntegerField with db_index True

> b. Name: value, data type:CharField with max_length=100

3. One view called fib_nums which caters the http get request from the front end.

## Frontend Design

The frontend is a modern React user interface with two pages, one with a simple form to get a input from user and the second to display the respective fibonacci numbers.

The API call is made when the user clicks on the submit button on the first page.

## Implementation Details

1. On loading the web app in the browser, the user will land on the first page where they can enter a valid integer(positive) n to generate the first n fibonacci numbers.

2. After entering the integer and clicking on the submit button, a check will be performed to see if the integer is valid, if not a message will be displayed to enter a valid integer.

3. If the integer is valid, an api call will be made to the backend to get the first n fibonacci numbers.

4. In the backend, I am using the sqlite3 database which comes with django framework, it will be first checked if the first n fibonacci numbers already exist in the database, if yes, they will be retrieved and a response will be sent back.

5. If they don't exist, the remaining fibonacci numbers are generated and saved in the database for future use and then the result is sent back.

6. In the front-end after getting the api response back, the data(fibonacci numbers) is transformed into needed form and displayed on a second page.

7. If there is any error during an api call, the error is caught and logged, which can be seen in the developer tools of the browser.

## Requirments

1. Please install Django in your machine, if not installed: **pip install django**

2. Please install Django CORS Headers package, if not installed: **pip install django-cors-headers**

3. Please install node, if not installed: **brew install node**

## Steps to run the project

### Steps to start the backend django server

1. go to the first_n_fib_nums directory and run the following cmd: **python manage.py runserver**

### Steps to start the frontend UI

1. go to the frontend_fib_nums directory and run the following cmd: **npm start**

The user interface will open up in the browser.

2. You can start generating fibonacci numbers now.
