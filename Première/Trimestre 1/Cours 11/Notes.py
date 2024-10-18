
"""Calculateur de Moyenne"""

def calculer_moyenne(notes):
    return sum(notes) / len(notes)

notes = []
for i in range(5):  # Supposons qu'on ait 5 matières
    note = float(input(f"Entrez la note pour la matière {i+1} : "))
    notes.append(note)

moyenne = calculer_moyenne(notes)
print(f"Votre moyenne est de : {moyenne:.2f}")
