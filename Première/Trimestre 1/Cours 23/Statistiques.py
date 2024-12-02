
"""Programme permettant de calculer des statistiques sur une liste"""

import statistics as stat # Import de la lib

# Focntion principale de calcule
def calcul_statistiques(data):
    etendue = max(data) - min(data)
    moyenne = stat.mean(data)
    median = stat.median(data) # Utilisation de la lib pour faire les calcules
    ecart_type = stat.stdev(data) if len(data) > 1 else 0 # Un écart type d'une série de 1 valeur vaut 0
    return (etendue, moyenne, median, ecart_type) # Return les valeurs dans un tuples

données = input("Entrez vos valeurs (séparées par des virgules) : ").split(", ") # Séparation du string dans une liste
données = [float(val) for val in données] # Convertissage des string en float

etendue, moyenne, median, ecart_type = calcul_statistiques(données)

print(f"\nL'étendue est de {etendue:.2f}.") # Print avec 2 chiffres après la virgule
print(f"La moyenne est de {moyenne:.2f}.")
print(f"La médianne est de {median:.2f}.")
print(f"L'écart type est de {ecart_type:.2f}.")