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

def add(nom, telephone, email):
    with sqlite3.connect(db_path) as connexion:
        curseur = connexion.cursor()
        curseur.execute(f'''
        INSERT INTO contacts (nom, telephone, email)
        VALUES ('{nom}', '{telephone}', '{email}');
        ''')
        connexion.commit()

def update_mail(name, email):
    with sqlite3.connect(db_path) as connexion:
        connexion.cursor().execute(f'''
        UPDATE contacts
        SET email = '{email}'
        WHERE nom = '{name}';
        ''')
        connexion.commit()

def read():
    with sqlite3.connect(db_path) as connexion:
        curseur = connexion.cursor()
        curseur.execute(f'''
        SELECT * FROM contacts;
        ''')
        print(curseur.fetchall())

def delete(name):
    with sqlite3.connect(db_path) as connexion:
        connexion.cursor().execute(f'''
        DELETE FROM contacts WHERE nom = '{name}';
        ''')
        connexion.commit()

if __name__ == '__main__':
    add('Alice', '0482469596', 'Alice@hotmail.com')
    read()
    update_mail('Alice', 'mail2@gmail.com')
    read()
    delete('Alice')
    read()

