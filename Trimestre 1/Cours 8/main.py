
# Initialisation des variables
total_essence = 0
distance_totale = 0

# Demander à l'utilisateur de saisir la consommation moyenne de son véhicule
consommation_moyenne = float(input("Entrez la consommation moyenne du véhicule (L/100km) : "))


# Boucle pour simuler plusieurs trajets
while True:
    # Demander la distance parcourue pour un trajet
    distance = float(input("Entrez la distance parcourue lors de ce trajet (km, 0 pour terminer) : "))

    if distance == 0: # Si la distance est 0, la simulation se termine
        break

    # Calculer la consommation d'essence pour ce trajet
    essence_utilisee = (distance / 100) * consommation_moyenne

    # Ajouter la consommation et la distance au total
    total_essence += essence_utilisee

distance_totale += distance

# Afficher la consommation pour ce trajet
print(f"Essence consommée pour ce trajet : {essence_utilisee:.2f} litres")

# Afficher la consommation totale et la distance totale à la fin
print(f"Distance totale parcourue : {distance_totale} km")
print(f"Essence totale consommée : {total_essence:.2f} litres")