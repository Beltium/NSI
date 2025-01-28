import sqlite3

def add_data(titre, description, date, catégorie):
    with sqlite3.connect("actus.db") as connexion:
        curseur = connexion.cursor()
        curseur.execute(f"""
        INSERT INTO actualites (titre, description, date, categorie)
        VALUES ('{titre}', '{description}', '{date}', '{catégorie}')
        """)
        connexion.commit()

actualites = [
    ("Élections Présidentielles", "Résultats des élections présidentielles 2023", "2024-05-01", "Politique"),
    ("Coupe du Monde de Football", "La finale de la Coupe du monde de fléchettes", "2024-12-18", "Sport"),
    ("Festival de Cannes", "Le célèbre festival de musique", "2024-05-14", "Culture"),
    ("Discours du Président", "Un discours marquant", "2024-07-01", "Politique")
]

# Insertion des actualités dans la table
for actualite in actualites:
    add_data(*actualite)
