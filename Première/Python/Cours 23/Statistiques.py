
"""Programme permettant de calculer des statistiques sur une liste"""

import statistics as stat # Import de la lib

# Focntion principale de calcule
def calcul_statistiques(data):
    etendue = max(data) - min(data)
    moyenne = stat.mean(data)
    median = stat.median(data) # Utilisation de la lib pour faire les calcules
    ecart_type = stat.stdev(data) if len(data) > 1 else 0 # Un écart type d'une série de 1 valeur vaut 0
    return (etendue, moyenne, median, ecart_type) # Return les valeurs dans un tuples


def main():
    while True:
        données = input("Entrez vos valeurs (séparées par des virgules) : ").split(", ")  # Séparation du string dans une liste

        try:
            données = [float(val) for val in données]  # Convertissage des string en float
        except ValueError:  # Gestion des erreurs en cas de string rentrés par l'utilisateur
            print("Erreur : Veuillez entrez uniquement des nombres séparés par des virgules.\n")
            continue # Si une erreur est détectée, on relance la boucle

        etendue, moyenne, median, ecart_type = calcul_statistiques(données)

        print(f"\nL'étendue est de {etendue:.2f}.")  # Print avec 2 chiffres après la virgule
        print(f"La moyenne est de {moyenne:.2f}.")
        print(f"La médianne est de {median:.2f}.")
        print(f"L'écart type est de {ecart_type:.2f}.")

        break # Si le programme s'est bien passé, on casse la boucle

if __name__ == '__main__':
    main()