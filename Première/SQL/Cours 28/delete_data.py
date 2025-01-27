import sqlite3

with sqlite3.connect("base_de_donnees.db") as connexion:
    curseur = connexion.cursor()

    curseur.execute('''
    DELETE FROM users
    WHERE age = 20
    ''')
    connexion.commit()