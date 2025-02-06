import sqlite3

db_path = 'contacts.db'

with sqlite3.connect(db_path) as connexion:
    curseur = connexion.cursor()
    curseur.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom VARCHAR(100),
                telephone VARCHAR(15),
                email VARCHAR(100)
            );
    ''')
    connexion.commit()
