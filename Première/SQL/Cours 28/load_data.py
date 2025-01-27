import sqlite3

connexion = sqlite3.connect("base_de_donnees.db")

curseur = connexion.cursor()

curseur.execute('SELECT * FROM users')

results = curseur.fetchall()

for user in results:
    print(f"ID: {user[0]}, Nom: {user[1]}, Email: {user[2]}, Âge: {user[3]}")

connexion.close()