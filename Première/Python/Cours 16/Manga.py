personnages = []

while True:
    # Menu pour les options disponibles
    print("\n1. Ajouter un personnage")
    print("2. Afficher les personnages")
    print("3. Quitter")

    choix = input("Que voulez-vous faire ? (1/2/3) : ")

    if choix == "1":
        # Ajout d'un nouveau personnage
        nom = input("Entrez le nom du personnage : ")
        age = int(input("Entrez l'âge du personnage : "))
        pouvoirs = input("Entrez les pouvoirs (séparés par des virgules) : ").split(',')

        # Ajout du personnage dans la liste
        personnages.append({
            "nom": nom,
            "age": age,
            "pouvoirs": [p.strip() for p in pouvoirs]  # Nettoie les espaces
        })

    elif choix == "2":
        # Affichage de tous les personnages
        if personnages:
            print("\nListe des personnages :")
            for personnage in personnages:
                print(
                    f"Nom : {personnage['nom']}, Âge : {personnage['age']}, Pouvoirs : {', '.join(personnage['pouvoirs'])}")
        else:
            print("Aucun personnage ajouté pour l'instant.")

    elif choix == "3":
        # Quitter le programme
        print("Merci d'avoir utilisé le gestionnaire de personnages !")
        break

    else:
        print("Choix invalide. Essayez encore.")