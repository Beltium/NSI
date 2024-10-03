
# Initialisation de la liste de personnages
personnages = []

def ajouter_personnage(nom, age, competences):
    personnage = {
        "nom": nom,
        "age": age,
        "competences": competences
    }
    personnages.append(personnage) # Ajoute le personnage à la liste
    print(f"{nom} a été ajouté à la liste des personnages.")

def supprimer_personnage(nom):
    for p in personnages:
        if nom in p['nom']:
            personnages.remove(p)
            print(f"{p['nom']} a été supprimé des personnages.")
            return 0

    print(f"{p['nom']} n'est pas dans la liste des personnages.")


def afficher_personnages():
    if personnages:
        print("Liste des personnages :")
        for p in personnages:
            print(f"Nom: {p['nom']}, Age: {p['age']}, Compétences: {', '.join(p['competences'])}")
    else:
        print("Aucun personnage dans la liste.")

# Menu principal
while True:
    print("\nMenu :")
    print("1. Ajouter un personnage")
    print("2. Supprimez un personnage")
    print("3. Afficher les personnages")
    print("4. Quitter")
    choix = input("Que voulez-vous faire ? (1/2/3/4) : ")

    if choix == "1":
        nom = input("Entrez le nom du personnage : ")
        age = int(input("Entrez l'âge du personnage : "))
        competences = input("Entrez les compétences (séparées par des virgules) : ").split(",")
        ajouter_personnage(nom, age, [c.strip() for c in competences]) # Nettoyer les espaces

    elif choix == "2":
        nom = input("Entrez le nom du personnage à supprimer : ")
        supprimer_personnage(nom)

    elif choix == "3":
        afficher_personnages()

    elif choix == "4":
        print("Merci d'avoir géré vos personnages !")
        break

    else:
        print("Choix invalide. Essayez encore.")