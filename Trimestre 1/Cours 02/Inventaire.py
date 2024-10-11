# Initialisation de l'inventaire
inventaire = []

def ajouter_objet(objet, nb):
    objetnb = [objet, nb] # Création d'une liste avec l'objet et son nombre
    inventaire.append(objetnb) # Ajoute l'objet à l'inventaire
    print(f"{objet} a été ajouté à votre inventaire en nombre de {nb}.")


def retirer_objet(objet):
    for i in inventaire:
        if objet in i: # Vérifier si l'objet est la liste de l'inventaire
            inventaire.remove(i) # Retire l'objet de l'inventaire
            print(f"{objet} a été retiré de votre inventaire.")
        else:
            print(f"{objet} n'est pas dans l'inventaire.")


def afficher_inventaire():
    if inventaire:
        print("Votre inventaire contient :")
        for objet in inventaire:
            print(" - " + objet[0] + "  x" +objet[1]) # Affiche chaque objet et leur nombre
    else:
        print("Votre inventaire est vide.")

def afficher_nb_objets():
    if inventaire:
        nb_objet_diff = len(inventaire) # Taille de la liste

        nb_objet = 0
        for objet in inventaire:
            nb_objet = nb_objet + int(objet[1]) # Ajout du nombre d'objet dans une variable

        print(f"Votre inventaire contient {nb_objet_diff} objets différents et {nb_objet} au total.")
    else:
        print("Votre inventaire est vide.")

def afficher_quantité_objet():
    if inventaire:
        nom_obj = input("De quelle objet voulez-vous voir le nombre ? ")
        trouve = False
        for objet in inventaire:
            if nom_obj in objet: # Vérifier si l'objet est présent
                print(f"Vous avez {objet[1]} {objet[0]}.") # Indiquer son nombre
                trouve = True
                break

        if not trouve: # Si il n'est pas trouvé, informer l'utilisateur
                print("Vous n'avez aucun n'exemplaire de cette objet.")

    else:
        print("Votre inventaire est vide.")


# Menu principal
while True:
    print("\nMenu :")
    print("1. Ajouter un objet")
    print("2. Retirer un objet")
    print("3. Afficher l'inventaire")
    print("4. Afficher le nombre d'objets de l'inventaire")
    print("5. Afficher la quantité d'un objet en particulier")
    print("6. Quitter")

    choix = input("Que voulez-vous faire ? (1/2/3/4/5/6) : ")

    if choix == "1":
        objet = input("Entrez le nom de l'objet à ajouter : ")
        nb = input("Combien en voulez vous ? ")
        ajouter_objet(objet, nb)

    elif choix == "2":
        objet = input("Entrez le nom de l'objet à retirer : ")
        retirer_objet(objet)

    elif choix == "3":
        afficher_inventaire()

    elif choix == "4":
        afficher_nb_objets()

    elif choix == "5":
        afficher_quantité_objet()

    elif choix == "6":
        print("Merci d'avoir joué !")
        break

    else:
        print("Choix invalide. Essayez encore.")