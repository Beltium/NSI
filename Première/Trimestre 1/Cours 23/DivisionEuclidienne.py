
"""Programme permettant de faire des divisons euclidiennes"""

# Fonction divison euclidienne
def div_eucli(a, b):

    if b == 0 :
        return None # Si le diviseur est égal à 0, ne rien renvoyer

    q = a // b
    r = a % b
    return (a, b) # Retrourner les résultats dans un tuples pour plus d'optimisation ;)

# Programme principal
dividende = 17
diviseur = 5

resultat = div_eucli(dividende, diviseur)

if resultat is None:
    print("Erreur : division par zéro.")
else:
    quotient, reste = resultat
    print(f"Le quotient de {dividende} divisé par {diviseur} est {quotient}.")
    print(f"Le reste de la division est {reste}.")