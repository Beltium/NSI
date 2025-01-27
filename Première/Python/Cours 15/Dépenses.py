total_depenses = 0

for i in range(3):
    try:
        depense = float(input("Entrez le montant de la dépense : "))

        if depense < 0:
            print("Montant invalide. Veuillez entrer un montant positif.")
        else:
            total_depenses += depense
            print(f"Dépense ajoutée. Total des dépenses : {total_depenses} €")
    except ValueError:
        print("Erreur : veuillez entrer un nombre valide.")

print(f"Le total de vos dépenses est de : {total_depenses} €")
