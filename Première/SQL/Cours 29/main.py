import sqlite3

db_path = "players.db"

def add_player(name, score, path=db_path):
    with sqlite3.connect(db_path) as connexion:
        curseur = connexion.cursor()
        curseur.execute(f'''
        INSERT INTO players (name, score)
        VALUES ('{name}', {score})
        ''')
        connexion.commit()

def input_player():
    while True:
        name = input("Entrer le nom du joueur ('fin' pour terminer) : ")
        if name == 'fin':
            break
        while True:
            try :
                score = int(input("Entrer son score : "))
            except ValueError:
                print("Veuillez rentrer un nombre entier.")
                continue
            break
        add_player(name, score)

def main():
    with sqlite3.connect(db_path) as connexion:
        curseur = connexion.cursor()
        curseur.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
        )
        ''')

