import sqlite3

with sqlite3.connect("base_de_donnees.db") as connexion:
    curseur = connexion.cursor()

    curseur.execute('''
    UPDATE users
    SET age = 20
    WHERE name = 'Bob Martin'
    ''')
    connexion.commit()