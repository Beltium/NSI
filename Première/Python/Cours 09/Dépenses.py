
def calculer_depenses():
    total, i, depense = 0, 0, 1
    while depense != 0: # Demande 3 montants par exemple
        i += 1
        depense = float(input(f"Entrez le montant de la dépense {i} : "))
        total += depense
    return total

# Appel de la fonction pour calculer les dépenses
total_depenses = calculer_depenses()
print("Le total des dépenses est :", total_depenses)