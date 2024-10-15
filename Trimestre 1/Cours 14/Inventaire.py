
"""Programme de Gestion d'Inventaire"""

# Fonctionnalité :
#     - Ajouter un objet à l'inventaire
#     - Afficher l'inventaire complet
#     - Accepter une quête
#     - Vendre un objet de l'inventaire
#     - Consulter le solde de pièces d'or

# Initialisation de l'inventaire, des quêtes et du solde d'or
inventaire = {
    "armes": [],
    "potions": [],
    "armures": []
}

quetes = {
    "qu1": {"nom": "Chasser le dragon", "objet_requis": "épée"},
    "qu2": {"nom": "Guérir le villageois", "objet_requis": "Potion de soin"}
}

prix_objets = {
    "épée": 50,  # Prix de vente pour chaque épée
    "Potion de soin": 10,  # Prix de vente pour chaque potion de soin
    "armure": 75  # Prix de vente pour chaque armure
}

or_joueur = 100  # Solde initial en pièces d'or


def afficher_inventaire():
    """Affiche tout l'inventaire, trié par catégorie."""
    print("\nInventaire complet :")
    for categorie, objets in inventaire.items():
        print(f"Catégorie : {categorie.capitalize()}")
        if objets:
            for item in objets:
                print(f" - {item[0]} : {item[1]} unités")
        else:
            print("  Aucun objet.")


def ajouter_objet():
    """Ajoute un objet à l'inventaire, avec une catégorie et une quantité."""
    print("Catégories disponibles : armes, potions, armures")
    categorie = input("Entrez la catégorie de l'objet : ").lower()

    if categorie in inventaire:
        objet = input(f"Entrez le nom de l'objet à ajouter dans {categorie} : ")
        quantite = int(input(f"Entrez la quantité de {objet} à ajouter : "))

        # Chercher si l'objet existe déjà dans cette catégorie
        trouve = False
        for item in inventaire[categorie]:
            if item[0] == objet:
                item[1] += quantite  # Augmenter la quantité si l'objet existe
                trouve = True
                break
        if not trouve:
            inventaire[categorie].append([objet, quantite])  # Ajouter le nouvel objet
    else:
        print("Catégorie invalide.")


def accepter_quete():
    """Permet d'accepter une quête et vérifie si l'utilisateur a l'objet requis pour la terminer."""
    print("\nQuêtes disponibles :")
    for code, quete in quetes.items():
        print(f"{code} : {quete['nom']} (Objet requis : {quete['objet_requis']})")

    choix_quete = input("Entrez le code de la quête que vous voulez accepter : ")

    if choix_quete in quetes:
        objet_requis = quetes[choix_quete]["objet_requis"]

        # Vérification dans toutes les catégories d'inventaire pour l'objet requis
        for objets in inventaire.values():
            for item in objets:
                if item[0] == objet_requis and item[1] > 0:
                    print(
                        f"Félicitations ! Vous avez terminé la quête '{quetes[choix_quete]['nom']}' car vous avez {objet_requis}.")
                    return
        print(f"Vous n'avez pas l'objet requis ({objet_requis}) pour terminer cette quête.")
    else:
        print("Quête invalide.")


def vendre_objet():
    """Permet de vendre un objet de l'inventaire pour gagner des pièces d'or."""
    global or_joueur

    print("Catégories disponibles : armes, potions, armures")
    categorie = input("Entrez la catégorie de l'objet à vendre : ").lower()

    if categorie in inventaire:
        objet = input(f"Entrez le nom de l'objet à vendre dans {categorie} : ")

        # Vérifier si l'objet est dans l'inventaire
        for item in inventaire[categorie]:
            if item[0] == objet:
                quantite_a_vendre = int(input(f"Combien de {objet} voulez-vous vendre ? "))

                if quantite_a_vendre <= item[1]:
                    # Calcul du prix total de la vente
                    if objet in prix_objets:
                        total_vente = quantite_a_vendre * prix_objets[objet]
                        or_joueur += total_vente
                        item[1] -= quantite_a_vendre  # Réduire la quantité dans l'inventaire
                        print(f"Vous avez vendu {quantite_a_vendre} {objet}(s) pour {total_vente} pièces d'or.")

                        if item[1] == 0:
                            inventaire[categorie].remove(item)  # Retirer l'objet s'il n'en reste plus
                    else:
                        print(f"Le prix pour {objet} n'est pas défini.")
                else:
                    print(f"Quantité insuffisante pour vendre {quantite_a_vendre} {objet}.")
                break
        else:
            print(f"{objet} n'est pas dans l'inventaire.")
    else:
        print("Catégorie invalide.")


def consulter_or():
    """Affiche le solde actuel de pièces d'or du joueur."""
    print(f"Vous avez actuellement {or_joueur} pièces d'or.")


# Menu principal
while True:
    print("\nMenu de gestion de l'inventaire et des quêtes :")
    print("1. Ajouter un objet")
    print("2. Afficher tout l'inventaire")
    print("3. Accepter une quête")
    print("4. Vendre un objet")
    print("5. Consulter pièces d'or")
    print("0. Quitter")

    choix = input("Entrez votre choix (1/2/3/4/5/0) : ")

    if choix == "1":
        ajouter_objet()
    elif choix == "2":
        afficher_inventaire()
    elif choix == "3":
        accepter_quete()
    elif choix == "4":
        vendre_objet()
    elif choix == "5":
        consulter_or()
    elif choix == "0":
        print("Merci d'avoir joué !")
        break
    else:
        print("Choix invalide, essayez encore.")
