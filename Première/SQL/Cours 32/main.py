import sqlite3

db_path = 'contacts.db'

with sqlite3.connect(db_path) as connexion:
    curseur = connexion.cursor()
    curseur.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom VARCHAR(100),
                telephone VARCHAR(15),
                email VARCHAR(100)
            );
    ''')
    connexion.commit()

def add():
    with sqlite3.connect(db_path) as connexion:
        curseur = connexion.cursor()
        curseur.execute('''
        INSERT INTO contacts (nom, telephone, email)
        VALUES ('Alice', '0645789716', 'aaaalice@gmail.com')
        ''')
        connexion.commit()

if __name__ == '__main__':
    add()