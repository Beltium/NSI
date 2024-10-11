# Initialisation des variables
total_revenus = 0
depenses = {}  # Dictionnaire pour les dépenses par catégorie

# Saisie des revenus
print("Entrez vos revenus :")
while True:
    revenu = float(input("Entrez un revenu (ou 0 pour terminer) : "))
    if revenu == 0:
        break
    total_revenus += revenu  # Ajoute le revenu au total

# Saisie des dépenses par catégorie
print("Entrez vos dépenses par catégorie (ex: loyer, nourriture, loisirs).")
print("Entrez 0 comme montant pour terminer.")
while True:
    categorie = input("Entrez la catégorie de dépense (ou 'fin' pour terminer) : ")
    if categorie.lower() == 'fin':  # Permet de sortir de la boucle
        break
    montant = float(input(f"Entrez le montant pour la catégorie '{categorie}' : "))
    if montant == 0:  # Si le montant est 0, on arrête l'entrée des dépenses
        break
    # Si la catégorie existe déjà, on ajoute au montant, sinon on la crée
    if categorie in depenses:
        depenses[categorie] += montant
    else:
        depenses[categorie] = montant

# Calcul du total des dépenses
total_depenses = sum(depenses.values())

# Calcul du solde final
solde = total_revenus - total_depenses

# Affichage du récapitulatif des dépenses par catégorie
print("\nRécapitulatif des dépenses par catégorie :")
for categorie, montant in depenses.items():
    print(f"{categorie.capitalize()} : {montant:.2f} €")

# Affichage du solde
print("\nSolde final :")
if solde > 0:
    print(f"Votre solde final est de {solde:.2f}€. Vous êtes en excédent.")
elif solde < 0:
    print(f"Votre solde final est de {solde:.2f}€. Vous êtes en déficit.")
else:
    print(f"Votre solde final est de {solde:.2f}€. Vous êtes à l'équilibre.")
