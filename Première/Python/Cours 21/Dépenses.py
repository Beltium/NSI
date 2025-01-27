# Dictionnaire pour les dépenses
depenses = {
    "loisir": [],
    "charges": []
}

def ajouter_depense(categorie):
    montant = float(input(f"\nEntrez le montant pour la catégorie {categorie} : "))
    depenses[categorie].append(montant)
    print(f"Dépense ajoutée dans {categorie} : {montant}€\n")

def afficher_depenses():
    print("\n=== Dépenses ===")
    for categorie, liste in depenses.items():
        print(f"{categorie.capitalize()} : {', '.join(f'{montant}€' for montant in liste)}")
        print(f"Total {categorie} : {sum(liste)}€\n")

# Menu principal
while True:
    print("1. Ajouter une dépense (Loisir)")
    print("2. Ajouter une dépense (Charges)")
    print("3. Afficher les dépenses")
    print("0. Quitter")
    choix = input("Choisissez une option (1/2/3/0) : ")

    match choix:
        case "1":
            ajouter_depense("loisir")
        case "2":
            ajouter_depense("charges")
        case "3":
            afficher_depenses()
        case "0":
            print("Merci d'avoir utilisé mon programme !")
            break
        case _:
            print("Option invalide. Veuillez réessayer.\n")
