# Zero-SQL with OpenAI


![F8D04628-B5E5-4707-B1A1-5D61C8516FA0](https://github.com/user-attachments/assets/543f901b-d2a3-4c93-85c6-cb283d10b782)


## Overview
Zero-SQL is a web-based application that generates and executes SQL queries based on natural language input using OpenAI's API. The application is built with Flask and Python, providing a user-friendly interface for generating SQL queries without needing SQL knowledge. It also executes the generated SQL queries on a local SQLite database and displays the results in a table format.

Details to the API: OpenAI Platform Documentation

## Requirements
To run this project, you'll need the following dependencies:

Flask
OpenAI API
SQLite3
You can install these dependencies using:

```bash
pip install -r requirements.txt
```


To start the application, run the following command:

```bash
python app.py
```

Once the server is running, you can access the web application at http://127.0.0.1:5000.

## Features
Natural Language to SQL Query Conversion: Enter your question or query in natural language, and OpenAI will generate the SQL code.
SQL Query Execution: The application automatically executes the generated SQL on a SQLite database.
Results Display: The query results are displayed in a formatted table for easy viewing.
How It Works
Enter your OpenAI API Key: Input your OpenAI API key to authenticate the request.
Provide a Query in Plain Language: Type a question or query in natural language (e.g., "Show the top-selling product").
Automatic SQL Generation: The application sends your query to OpenAI to generate the corresponding SQL statement.
SQL Execution and Results Display: The SQL is executed on the SQLite database, and the results are shown in a table on the web page.

## Demo
Currently unavailable.

## Credits
This project was created with Python and Flask, leveraging OpenAI's API for natural language processing assistance.

