jeux_video = []

while True:
    print("\n1. Ajouter un jeu")
    print("2. Supprimer un jeu")
    print("3. Rechercher un jeu")
    print("4. Afficher la liste")
    print("5. Quitter")
    choix = input("Choisissez une option : ")

    if choix == "1":
        jeu = input("Entrez le nom d'un jeu vidéo à ajouter : ")
        jeux_video.append(jeu)
        print(f"{jeu} a été ajouté.")
    elif choix == "2":
        jeu = input("Entrez le nom d'un jeu vidéo à supprimer : ")
        if jeu in jeux_video:
            jeux_video.remove(jeu)
            print(f"{jeu} a été supprimé.")
        else:
            print(f"{jeu} n'est pas dans la liste.")
    elif choix == "3":
        jeu = input("Entrez le nom d'un jeu vidéo à rechercher : ")
        if jeu in jeux_video:
            print(f"{jeu} est dans la liste.")
        else:
            print(f"{jeu} n'est pas dans la liste.")
    elif choix == "4":
        print("Liste des jeux vidéo :")
        for j in jeux_video:
            print(j)
    elif choix == "5":
        break
    else:
        print("Option invalide.")
