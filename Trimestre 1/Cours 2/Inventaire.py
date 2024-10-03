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


# Menu principal
while True:
    print("\nMenu :")
    print("1. Ajouter un objet")
    print("2. Retirer un objet")
    print("3. Afficher l'inventaire")
    print("4. Quitter")

    choix = input("Que voulez-vous faire ? (1/2/3/4) : ")

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
        print("Merci d'avoir joué !")
        break

    else:
        print("Choix invalide. Essayez encore.")