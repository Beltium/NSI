import json

# Nom du fichier pour sauvegarder les données
file = "mangas.json"

# Charger les données du fichier s'il existe
try:
    with open(file, "r") as fichier:
        mangas = json.load(fichier)
except FileNotFoundError:
    mangas = {}

print("Bienvenue dans votre gestionnaire de mangas !\n")
if mangas:
    print("Voici votre liste actuelle de mangas :")
    for titre, episodes in mangas.items():
        print(f"{titre}: {episodes} épisodes vus")
else:
    print("Votre liste de mangas est vide. Commencez à en ajouter !")

# Boucle principale du programme
while True:
    print("\nOptions :")
    print("1. Ajouter un nouveau manga")
    print("2. Modifier le nombre d'épisodes vus")
    print("3. Ajout rapide")
    print("4. Afficher la liste des mangas")
    print("5. Supprimer un manga")
    print("0. Quitter")

    choix = input("Entrez votre choix (1/2/3/4/5/0) : ")

    match choix:

        # Ajouter un nouveau manga
        case "1":
            titre = input("Entrez le titre du manga : ")
            episodes = int(input(f"Combien d'épisodes avez-vous vus de {titre} ? "))
            mangas[titre] = episodes
            print(f"{titre} a été ajouté avec {episodes} épisodes vus.")

        # Modifier le nombre d'épisodes pour un manga existant
        case "2":
            titre = input("Entrez le titre du manga à modifier : ")
            if titre in mangas:
                nouveaux_episodes = int(input(f"Combien d'épisodes avez-vous vus maintenant pour {titre} ? "))
                mangas[titre] = nouveaux_episodes
                print(f"Le nombre d'épisodes vus pour {titre} a été mis à jour.")
            else:
                print(f"{titre} n'est pas dans la liste des mangas.")

        # Ajout rapide
        case "3":
            titre = input("Entrez le titre du manga à modifier : ")
            if titre in mangas:
                new_ep = int(input(f"Combien d'épisodes avez-vous vus en plus pour {titre} ? "))
                mangas[titre] += new_ep
                print(f"Ajout de {new_ep} épisodes à {titre}...")
                print(f"Le nombre d'épisodes vus pour {titre} a été mis à jour, vous êtes maintenant à {mangas[titre]}.")
            else:
                print(f"{titre} n'est pas dans la liste des mangas.")


        # Afficher la liste des mangas et des épisodes
        case "4":
            if mangas:
                print("Liste des mangas suivis :")
                for titre, episodes in mangas.items():
                    print(f"{titre}: {episodes} épisodes vus")
            else:
                print("La liste des mangas est vide.")

        # Supprimer un manga
        case "5":
            titre = input("Entrez le titre du manga à supprimer : ")
            if titre in mangas:
                del mangas[titre]
                print(f"{titre} a été supprimé de la liste.")
            else:
                print(f"{titre} n'est pas dans la liste.")

        # Quitter le programme
        case "0":
            # Sauvegarder les données avant de quitter
            with open(file, "w") as fichier:
                json.dump(mangas, fichier, indent=5)
            print("Merci d'avoir utilisé le gestionnaire de suivi d'épisodes.")
            break

        # Gestion d'un choix invalide
        case _:
            print("Choix invalide. Essayez encore.")
