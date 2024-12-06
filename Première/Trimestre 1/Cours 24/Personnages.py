
import json
from logging import exception

# Initiation des variables
characters = {}
file_path = "personnages.json"

def save_to_json(dictionary, file_path = file_path):
    try:
        with open(file_path, 'w') as json_file:
            json.dump(dictionary, json_file, indent=5)
        print(f"Sauvegarde effectuée avec succès dans : {file_path}")
    except Exception as e:
        print(f"Une erreur s'est produite pendant la sauvegarde : {e}")


def read_from_json(file_path = file_path):
    try:
        with open(file_path, 'r') as json_file:
            dictionary = json.load(json_file)
        print(f"Données lues avec succèes depuis : {file_path}")
        return dictionary
    except Exception as e:
        print(f"Une erreur s'est produite pendant la sauvegarde : {e}")
        return {}

def add_character():
    while True:
        name = input("Entrez le nom du personnage : ")

        try :
            age = int(input(f"Entrez l'age de {name} : "))
        except ValueError:
            print("Erreur : Veuillez entrez une valeur numérique pour l'âge.")
            continue

        role = input(f"Entrez le rôle de {name} : ")
        skills = input(f"Entrez les compétences de {name} (séparé par des virgules) : ").split(", ")

        inventory = {}
        while True:
            item = input("Entrez un objet à rajouter à l'inventaire : ")
            if item.lower() == 'fin':
                break
            try:
                quantity = int(input(f"Combien de {item} faut-il ajouter ? "))
            except ValueError:
                print("Erreur : Veuillez entrz une valeur numérique pour la quantité.")
                continue
            inventory[item] = quantity

        characters[name] = {
            "age": age,
            "role": role,
            "skills": tuple(skills),
            "inventory": inventory
        }
        print(f"{name} a été ajouté avec succés.\n")
        break

def display_characters():
    if not characters:
        print("Aucun personnage enregistré.\n")

    for name, info in characters.items():
        print(f"  Nom : {name}")
        print(f"  Âge : {info['age']}")
        print(f"  Rôle : {info['role']}")
        print(f"  Compétences : {', '.join(info['skills'])}")
        print(f"  Inventaire :")
        for item, quantity in info['inventory'].items():
            print(f"    {item} : {quantity}")
        print()

def menu():
    print(r"""
     ██████╗██╗  ██╗ █████╗ ██████╗  █████╗  ██████╗████████╗███████╗██████╗ ███████╗
    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝
    ██║     ███████║███████║██████╔╝███████║██║        ██║   █████╗  ██████╔╝███████╗
    ██║     ██╔══██║██╔══██║██╔══██╗██╔══██║██║        ██║   ██╔══╝  ██╔══██╗╚════██║
    ╚██████╗██║  ██║██║  ██║██║  ██║██║  ██║╚██████╗   ██║   ███████╗██║  ██║███████║
     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝

     Gestion des personnages - Jeux-Vidéos & Mangas
            """)

    global characters
    characters = read_from_json()
    while True:
        print("======= Menu =======")
        print("1. Ajouter un personnage")
        print("2. Afficher les personnages")
        print("0. Quitter le programme")

        choice = input("Que voulez-vous faire ? (1/2/0) ")
        match choice:

            case "1":
                add_character()
                save_to_json(characters)
            case "2":
                display_characters()
            case "0":
                print("Merci d'avoir utilisé mon programme !")
                exit()

if __name__ == '__main__':
    menu()