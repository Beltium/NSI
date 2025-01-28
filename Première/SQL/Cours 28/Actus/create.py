import sqlite3

connexion = sqlite3.connect("actus.db")


curseur = connexion.cursor()
curseur.execute('''
CREATE TABLE IF NOT EXISTS actualites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    description TEXT NOT NULL,
    date TEXT NOT NULL,
    categorie TEXT NOT NULL
)
''')

connexion.commit()
connexion.close()