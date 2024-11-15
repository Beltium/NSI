quetes = []
quetes_terminees = []

while True:
    print("\nQue voulez-vous faire ?")
    print("1. Ajouter une quête")
    print("2. Marquer une quête comme terminée")
    print("3. Afficher les quêtes")
    print("4. Modifier une quête")
    print("5. Supprimer une quête")
    print("0. Quitter")

    choix = input("Entrez votre choix (1/2/3/4/5/0) : ")

    if choix == "1":
        nouvelle_quete = input("Entrez la description de la nouvelle quête : ")
        quetes.append(nouvelle_quete)
        print(f"La quête '{nouvelle_quete}' a été ajoutée.")

    elif choix == "2":
        if not quetes:
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

    elif choix == "3":
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

    elif choix == "4":
        if not quetes:
            print("Aucune quête en cours.")
        else:
            print("Quêtes en cours :")
            for i, quete in enumerate(quetes):
                print(f"{i + 1}. {quete}")
            quete_modif = int(input("Entrez le numéro de la quête à modifier : ")) - 1
            if 0 <= quete_modif < len(quetes):
                nouvelle_description = input("Entrez la nouvelle description de la quête : ")
                quetes[quete_modif] = nouvelle_description
                print("Quête modifiée.")
            else:
                print("Numéro de quête invalide.")

    elif choix == "5":
        if not quetes:
            print("Aucune quête en cours.")
        else:
            print("Quêtes en cours :")
            for i, quete in enumerate(quetes):
                print(f"{i + 1}. {quete}")
            quete_supp = int(input("Entrez le numéro de la quête à supprimer : ")) - 1
            if 0 <= quete_supp < len(quetes):
                quetes.pop(quete_supp)
                print("Quête supprimée.")
            else:
                print("Numéro de quête invalide.")

    elif choix == "0":
        print("Merci d'avoir géré vos quêtes !")
        break

    else:
        print("Choix invalide. Essayez encore.")
