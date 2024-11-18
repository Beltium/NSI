films = []

while True:
    print("\n1. Ajouter un film")
    print("2. Noter un film")
    print("3. Supprimer un film")
    print("4. Afficher les films et notes")
    print("5. Quitter")
    choix = input("Choisissez une option : ")

    if choix == "1":
        film = input("Entrez le nom d'un film à ajouter : ")
        if film not in films:
            films.append({"nom": film, "note": None})
            print(f"{film} a été ajouté.")
        else:
            print(f"{film} est déjà dans la liste.")
    elif choix == "2":
        film = input("Entrez le nom du film à noter : ")
        for f in films:
            if f["nom"] == film:
                note = input("Entrez une note (sur 10) : ")
                f["note"] = note
                print(f"{film} a été noté {note}/10.")
                break
        else:
            print(f"{film} n'est pas dans la liste.")
    elif choix == "3":
        film = input("Entrez le nom d'un film à supprimer : ")
        for f in films:
            if f["nom"] == film:
                films.remove(f)
                print(f"{film} a été supprimé.")
                break
        else:
            print(f"{film} n'est pas dans la liste.")
    elif choix == "4":
        print("Liste des films :")
        if not films:
            print("Aucun film dans la liste.")
        for f in films:
            print(f"- {f['nom']} (Note : {f['note'] if f['note'] else 'Non noté'})")
    elif choix == "5":
        break
    else:
        print("Option invalide.")
