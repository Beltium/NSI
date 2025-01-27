quetes = []  # Liste pour stocker les quêtes en cours
quetes_terminees = []  # Liste pour stocker les quêtes terminées

while True:
    print("\nQue voulez-vous faire ?")
    print("1. Ajouter une quête")
    print("2. Marquer une quête comme terminée")
    print("3. Afficher les quêtes")
    print("0. Quitter")

    choix = input("Entrez votre choix (1/2/3/0) : ")

    if choix == "1":  # Ajouter une quête
        nouvelle_quete = input("Entrez la description de la nouvelle quête : ")
        quetes.append(nouvelle_quete)
        print(f"La quête '{nouvelle_quete}' a été ajoutée.")

    elif choix == "2":  # Marquer une quête comme terminée
        if not quetes:  # Vérifie si la liste des quêtes en cours est vide
            print("Aucune quête en cours.")
        else:
            print("Quêtes en cours :")
            for i, quete in enumerate(quetes):
                print(f"{i + 1}. {quete}")
            quete_terminee = int(input("Entrez le numéro de la quête terminée : ")) - 1
            if 0 <= quete_terminee < len(quetes):
                quetes_terminees.append(quetes.pop(quete_terminee))
                print("Quête terminée.")
            else:
                print("Numéro de quête invalide.")

    elif choix == "3":  # Afficher les quêtes
        if quetes:
            print("\nQuêtes en cours :")
            for quete in quetes:
                print("-", quete)
        else:
            print("\nAucune quête en cours.")

        if quetes_terminees:
            print("\nQuêtes terminées :")
            for quete in quetes_terminees:
                print("-", quete)
        else:
            print("\nAucune quête terminée.")

    elif choix == "0":  # Quitter
        print("Merci d'avoir géré vos quêtes !")
        break

    else:
        print("Choix invalide. Essayez encore.")