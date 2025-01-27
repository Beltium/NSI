import json

# Nom du fichier pour sauvegarder les données
file = "notes.json"

# Charger les données du fichier s'il existe
try:
    with open(file, "r") as fichier:
        notes = json.load(fichier)
except FileNotFoundError:
    notes = {}

def save_data():
    with open(file, "w") as fichier:
        json.dump(notes, fichier, indent=4)

def ajouter_note(matiere, note):
    if matiere not in notes:
        notes[matiere] = []
    notes[matiere].append(note)
    print(f"Note ajoutée à {matiere}: {note}")
    save_data()

def moyenne_par_matiere(matiere):
    if matiere in notes and notes[matiere]:
        return sum(notes[matiere]) / len(notes[matiere])
    else:
        print(f"Aucune note enregistrée pour {matiere}.")
        return None

def moyenne_globale():
    total_notes = 0
    total_matiere = 0
    for matiere, liste_notes in notes.items():
        total_notes += sum(liste_notes)
        total_matiere += len(liste_notes)
    return total_notes / total_matiere if total_matiere > 0 else None

def afficher_notes():
    if not notes:
        print("Aucune note enregistrée.")
        return
    print("Notes enregistrées :")
    for matiere, liste_notes in notes.items():
        print(f"{matiere}: {liste_notes}")
    save_data()

# Menu principal
def menu():
    while True:
        print("\n--- Gestion des Notes ---")
        print("1. Ajouter une note")
        print("2. Afficher les notes")
        print("3. Calculer la moyenne d'une matière")
        print("4. Calculer la moyenne globale")
        print("5. Quitter")
        choix = input("Choisissez une option : ")

        match choix:
            case "1":
                matiere = input("Entrez le nom de la matière : ")
                try:
                    note = float(input("Entrez la note (0-20) : "))
                    if 0 <= note <= 20:
                        ajouter_note(matiere, note)
                    else:
                        print("La note doit être entre 0 et 20.")
                except ValueError:
                    print("Entrez une note valide.")
            case "2":
                afficher_notes()
            case "3":
                matiere = input("Entrez le nom de la matière : ")
                moyenne = moyenne_par_matiere(matiere)
                if moyenne is not None:
                    print(f"Moyenne de {matiere}: {moyenne:.2f}")
            case "4":
                moyenne = moyenne_globale()
                if moyenne is not None:
                    print(f"Moyenne globale: {moyenne:.2f}")
                else:
                    print("Aucune note pour calculer la moyenne globale.")
            case "5":
                print("Merci d'avoir utilisé mon programme")
                break
            case _:
                print("Choix invalide. Réessayez.")

if __name__ == '__main__':
    menu()
