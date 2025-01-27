
def calculer_participation(votants, electeurs_totaux):
    return (votants / electeurs_totaux) * 100

votants = int(input("Entrez le nombre de votants : "))
electeurs_totaux = int(input("Entrez le nombre total d'électeurs : "))
participation = calculer_participation(votants, electeurs_totaux)
print(f"Le pourcentage de participation est : {participation:.2f}%")