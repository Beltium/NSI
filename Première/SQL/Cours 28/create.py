import sqlite3

connexion = sqlite3.connect("base_de_donnees.db")


curseur = connexion.cursor()
curseur.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
)
''')

connexion.commit()
connexion.close()