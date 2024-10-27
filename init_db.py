import sqlite3

def initialize_database():
    # Verbindung zur SQLite-Datenbank herstellen (erstellt eine neue Datei falls sie nicht existiert)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Tabellen für Produkte und Bestellungen erstellen
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Produkte (
            ProduktID INTEGER PRIMARY KEY AUTOINCREMENT,
            Produktname TEXT NOT NULL,
            Preis REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Bestellungen (
            BestellungID INTEGER PRIMARY KEY AUTOINCREMENT,
            ProduktID INTEGER NOT NULL,
            Menge INTEGER NOT NULL,
            Bestelldatum TEXT NOT NULL,
            Person TEXT NOT NULL,
            FOREIGN KEY (ProduktID) REFERENCES Produkte(ProduktID)
        )
    ''')

    # Beispieldaten in die Produkte-Tabelle einfügen, falls diese leer ist
    cursor.execute("SELECT COUNT(*) FROM Produkte")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Produkte (Produktname, Preis) VALUES ('Laptop', 999.99)")
        cursor.execute("INSERT INTO Produkte (Produktname, Preis) VALUES ('Smartphone', 699.99)")
        cursor.execute("INSERT INTO Produkte (Produktname, Preis) VALUES ('Tablet', 399.99)")

    # Beispieldaten in die Bestellungen-Tabelle einfügen, falls diese leer ist
    cursor.execute("SELECT COUNT(*) FROM Bestellungen")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO Bestellungen (ProduktID, Menge, Bestelldatum, Person) VALUES (1, 2, '2024-10-20', 'Max Mustermann')")
        cursor.execute("INSERT INTO Bestellungen (ProduktID, Menge, Bestelldatum, Person) VALUES (2, 1, '2024-10-21', 'Erika Musterfrau')")
        cursor.execute("INSERT INTO Bestellungen (ProduktID, Menge, Bestelldatum, Person) VALUES (3, 3, '2024-10-22', 'Hans Meier')")

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()
