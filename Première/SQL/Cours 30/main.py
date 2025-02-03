import sqlite3
import datetime

# Chemin de la base de données
db_path = "expenses.db"


def add_expense(expense_type, amount, date, path=db_path):
    """Ajoute une dépense dans la base de données."""
    try:
        with sqlite3.connect(path) as connexion:
            curseur = connexion.cursor()
            curseur.execute(f'''
                INSERT INTO expenses (type, amount, date)
                VALUES ('{expense_type}', {amount}, '{date}')
            ''')
            connexion.commit()
            print(f"Dépense '{expense_type}' de {amount}€ ajoutée le {date}.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de la dépense : {e}")


def input_expense():
    """Saisie des dépenses par l'utilisateur."""
    while True:
        expense_type = input("Entrer le type de dépense ('fin' pour terminer) : ")
        if expense_type.lower() == 'fin':
            break
        while True:
            try:
                amount = float(input("Entrer le montant : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre valide pour le montant.")

        # Demander la date de la dépense, ou utiliser la date du jour si non renseignée
        date_input = input("Entrer la date (format AAAA-MM-JJ) ou appuyer sur Entrée pour aujourd'hui : ")
        if not date_input:
            date_input = datetime.date.today().strftime("%Y-%m-%d")

        add_expense(expense_type, amount, date_input)


def display_expenses(path=db_path):
    """Affiche toutes les dépenses enregistrées."""
    with sqlite3.connect(path) as connexion:
        curseur = connexion.cursor()
        curseur.execute('''
            SELECT type, amount, date FROM expenses
            ORDER BY date DESC;
        ''')
        expenses = curseur.fetchall()
        if not expenses:
            print("Aucune dépense enregistrée.")
        else:
            print("\nListe des dépenses :")
            for expense in expenses:
                print(f"Type : {expense[0]}, Montant : {expense[1]}€, Date : {expense[2]}")


def main():
    # Création de la table 'expenses' si elle n'existe pas déjà
    with sqlite3.connect(db_path) as connexion:
        curseur = connexion.cursor()
        curseur.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        connexion.commit()

    # Menu principal
    while True:
        print("\n==== MENU ====")
        print("1. Ajouter une dépense.")
        print("2. Afficher toutes les dépenses.")
        print("0. Quitter.")
        choice = input("Entrer votre choix (1/2/0) : ")
        if choice == '1':
            input_expense()
        elif choice == '2':
            display_expenses()
        elif choice == '0':
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == '__main__':
    main()
