from flask import Flask, render_template, request, redirect, url_for, session, flash
from openai import OpenAI
from init_db import initialize_database  # Initialisierungsskript importieren
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Ersetze dies durch einen sicheren Schlüssel


# Datenbank initialisieren
initialize_database()


# Startseite mit Formular für Eingabe und API-Key
@app.route('/', methods=['GET', 'POST'])
def index():
    sql_query = None
    results = None
    if request.method == 'POST':
        print("POST request received")  # Debugging-Ausgabe
        api_key = request.form.get('api_key')
        user_input = request.form.get('user_input')

        if not api_key:
            flash("API-Key ist erforderlich.", "danger")
            return redirect(url_for('index'))
        
        if not user_input:
            flash("Eine Anfrage ist erforderlich.", "danger")
            return redirect(url_for('index'))

        # API-Schlüssel und Kontext setzen
        session['api_key'] = api_key
        client = OpenAI(api_key=api_key)


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

        # OpenAI-Aufruf mit Fehlermanagement
        try:
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
            #print(response)

            sql_query = response.choices[0].message.content.strip()

              # SQL-Abfrage in SQLite-Datenbank ausführen
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(sql_query)
            results = cursor.fetchall()  # Alle Ergebnisse abrufen
            column_names = [description[0] for description in cursor.description]  # Spaltennamen abrufen
            conn.close()

            return render_template('index.html', sql_query=sql_query, results=results, column_names=column_names)


        except Exception as e:
            flash(f"Ein unerwarteter Fehler ist aufgetreten: {str(e)}", "danger")
        
        return redirect(url_for('index'))
    
    return render_template('index.html', sql_query=None, results=None, column_names=None)

if __name__ == '__main__':
    app.run(debug=True)
