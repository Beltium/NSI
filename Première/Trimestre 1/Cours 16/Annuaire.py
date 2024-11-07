contacts = []

while True:
    # Menu
    print("\n1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Quitter")

    choix = input("Que voulez-vous faire ? (1/2/3) : ")

    if choix == "1":
        nom = input("Entrez le nom du contact : ")
        numero = input("Entrez le numéro de téléphone : ")
        adresse = input("Entrez l'adresse : ")

        contacts.append({
            "nom": nom,
            "numero": numero,
            "adresse": adresse
        })
        print(f"Contact '{nom}' ajouté avec succès.")

    elif choix == "2":
        if contacts:
            print("\nListe des contacts :")
            for contact in contacts:
                print(f"Nom : {contact['nom']}, Téléphone : {contact['numero']}, Adresse : {contact['adresse']}")
        else:
            print("Aucun contact ajouté pour l'instant.")

    elif choix == "3":
        # Quitter le programme
        print("Merci d'avoir utilisé l'annuaire de contacts !")
        break

    else:
        print("Choix invalide. Essayez encore.")
