# Initialisation des votes
votes = {}

while True:
    candidat = input("Entrez le nom du candidat (ou 'fin' pour terminer) : ")
    if candidat.lower() == 'fin':
        break
    nb_votes = int(input(f"Entrez le nombre de votes pour {candidat} : "))
    votes[candidat] = nb_votes

# Affichage des résultats
print("Résultats des votes :")
for candidat, nb_votes in votes.items():
    print(f"{candidat} : {nb_votes} votes")