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

## Messages
The magic part is in the messages section. Here you can specify the tables and the output of the message.
```python
 system_context = """Given the following SQL tables, your job is to write queries given a user’s request.
                            -- Tabelle für Produkte
                            CREATE TABLE Produkte (
                                ProduktID INT PRIMARY KEY AUTO_INCREMENT,
                                Produktname VARCHAR(100) NOT NULL,
                                Preis DECIMAL(10, 2) NOT NULL
                            );

                            -- Tabelle für Bestellungen
                            CREATE TABLE Bestellungen (
                                BestellungID INT PRIMARY KEY AUTO_INCREMENT,
                                ProduktID INT NOT NULL,
                                Menge INT NOT NULL,
                                Bestelldatum DATE NOT NULL,
                                Person VARCHAR(100) NOT NULL,
                                FOREIGN KEY (ProduktID) REFERENCES Produkte(ProduktID)
                            );
                         """

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_context},
                    {"role": "user", "content": f"Generate the SQL query for: {user_input}. Only output the raw SQL query without any code block delimiters or markdown."}

                ],
                response_format={
                    "type": "text"
                }
            )
```

## Features
Natural Language to SQL Query Conversion: Enter your question or query in natural language, and OpenAI will generate the SQL code.
SQL Query Execution: The application automatically executes the generated SQL on a SQLite database.
Results Display: The query results are displayed in a formatted table for easy viewing.

## How It Works
Enter your OpenAI API Key: Input your OpenAI API key to authenticate the request.
Provide a Query in Plain Language: Type a question or query in natural language (e.g., "Show the top-selling product").
Automatic SQL Generation: The application sends your query to OpenAI to generate the corresponding SQL statement.
SQL Execution and Results Display: The SQL is executed on the SQLite database, and the results are shown in a table on the web page.

## Demo
Currently unavailable.

## Credits
This project was created with Python and Flask, leveraging OpenAI's API for natural language processing assistance.

