import sqlite3

connexion = sqlite3.connect("base_de_donnees.db")

curseur = connexion.cursor()

curseur.execute('''
INSERT INTO users (name, email, age)
VALUES ('Jean Dupont', 'jean.d@gmail.com', 25)
''')

curseur.execute('''
INSERT INTO users (name, email, age)
VALUES ('Bob Martin', 'bob.m@gmail.com', 35)
''')

connexion.commit()
connexion.close()