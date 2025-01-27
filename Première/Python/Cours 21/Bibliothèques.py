# Dictionnaire pour la bibliothèque
bibliotheque = {}

def ajouter_livre():
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez l'auteur du livre : ")
    statut = input("Statut de lecture (non lu/en cours de lecture/lu) : ")
    bibliotheque[titre] = {"auteur": auteur, "statut": statut}
    print(f"Le livre '{titre}' a été ajouté à la bibliothèque.\n")

def afficher_livres():
    if not bibliotheque:
        print("La bibliothèque est vide.\n")
        return
    print("\n=== Liste des livres ===")
    for titre, details in bibliotheque.items():
        print(f"- {titre} de {details['auteur']} ({details['statut']})")
    print()

def modifier_statut():
    titre = input("Entrez le titre du livre à modifier : ")
    if titre in bibliotheque:
        nouveau_statut = input("Nouveau statut (non lu/en cours de lecture/lu) : ")
        bibliotheque[titre]["statut"] = nouveau_statut
        print(f"Le statut de '{titre}' a été mis à jour.\n")
    else:
        print(f"Le livre '{titre}' n'existe pas dans la bibliothèque.\n")

# Menu principal
while True:
    print("1. Ajouter un livre")
    print("2. Afficher tous les livres")
    print("3. Modifier le statut d'un livre")
    print("4. Quitter")
    choix = input("Choisissez une option : ")

    match choix:
        case "1":
            ajouter_livre()
        case "2":
            afficher_livres()
        case "3":
            modifier_statut()
        case "4":
            print("Merci d'avoir utilisé la bibliothèque !")
            break
        case _:
            print("Option invalide. Veuillez réessayer.\n")
