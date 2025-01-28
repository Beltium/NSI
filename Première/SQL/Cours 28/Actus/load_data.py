import sqlite3

db = "actus.db"

def load_data(prompt, db = db):
    with sqlite3.connect(db) as connexion:
        curseur = connexion.cursor()
        curseur.execute(prompt)
        return curseur.fetchall()

prompt = '''
SELECT * FROM actualites WHERE titre LIKE '%Coupe%';
'''

print(load_data(prompt))