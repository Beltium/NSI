# Dictionnaire pour stocker les mangas et le nombre d'épisodes vus
mangas = {}

# Boucle principale du programme
while True:
    print("\nOptions :")
    print("1. Ajouter un nouveau manga")
    print("2. Modifier le nombre d'épisodes vus")
    print("3. Afficher la liste des mangas")
    print("4. Supprimer un manga")
    print("0. Quitter")

    choix = input("Entrez votre choix (1/2/3/4/0) : ")

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

        # Afficher la liste des mangas et des épisodes
        case "3":
            print("Liste des mangas suivis :")
            for titre, episodes in mangas.items():
                print(f"{titre}: {episodes} épisodes vus")



        case "4":  # Supprimer un manga
            titre = input("Entrez le titre du manga à supprimer : ")
            if titre in mangas:
                del mangas[titre]
                print(f"{titre} a été supprimé de la liste.")
            else:
                print(f"{titre} n'est pas dans la liste.")

        # Quitter le programme
        case "0":
            print("Merci d'avoir utilisé le gestionnaire de suivi d'épisodes.")
            break

        # Gestion d'un choix invalide
        case _:
            print("Choix invalide. Essayez encore.")