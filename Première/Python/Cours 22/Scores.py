scores = []

# Boucle pour entrer les scores
while True:
    score = input("Entrez un score (ou 'fin' pour terminer) : ")
    if score.lower() == "fin":  # Si l'utilisateur entre 'fin', on termine la saisie
        break
    score = int(score)  # Convertit l'entrée en entier
    scores.append(score)  # Ajoute le score à la liste

# Afficher les scores
print("Scores des joueurs :")
for i in range(len(scores)):
    print(f"Joueur {i + 1}: {scores[i]}")

# Tri des scores dans l'ordre décroissant
scores.sort(reverse=True)

# Afficher les scores triés
print("\nScores des joueurs (du meilleur au moins bon) :")
for i in range(len(scores)):
    print(f"Joueur {i + 1}: {scores[i]}")

moyenne = sum(scores) / len(scores)
print(f"\nLa moyenne des scores est : {moyenne:.2f}")