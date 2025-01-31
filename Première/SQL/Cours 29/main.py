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
        print(f"{name} ajouté avec succès avec un score de {score}.")

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

def display_players(path=db_path):
    with sqlite3.connect(path) as connexion:
        curseur = connexion.cursor()
        curseur.execute('''
        
        ''')
        return curseur.fetchall()

def main():
    with sqlite3.connect(db_path) as connexion:
        curseur = connexion.cursor()
        curseur.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL
        )''')

        while True:
            print("==== MENU ====")
            print("1. AJouter un score.")
            print("2. Afficher les 3 meilleurs scores.")
            print("0. Quitter.")
            choice = input("Entrer votre choix (1/2/0) : ")
            match choice:
                case '1':
                    input_player()
                    continue
                case '2':
                    print("a")
                    continue
                case '0':
                    exit()
                case _:
                    print("Veuiller choisir un score ")

if __name__ == '__main__':
    main()