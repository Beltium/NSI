import sqlite3

db_path = "players.db"

with sqlite3.connect(db_path) as connexion:
    curseur = connexion.cursor()
    curseur.execute('''
    CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score INTEGER NOT NULL,
    )
    ''')

def add_player(name, score, path=db_path):
    with sqlite3.connect(db_path) as connexion:
        curseur = connexion.cursor()
        curseur.execute(f'''
        INSERT INTO players (name, score)
        VALUES ('{name}', {score})
        ''')
        connexion.commit()

