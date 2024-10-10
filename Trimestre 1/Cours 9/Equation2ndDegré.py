
"""Résolveur d'équations du second degré dans C"""

from cmath import sqrt

def delta(a, b, c):
    delta_value = b**2 - 4*a*c

    if delta_value > 0:
        x1 = (-b - sqrt(delta_value)) / (2 * a)
        x2 = (-b + sqrt(delta_value)) / (2 * a)
        return [x1, x2]

    if delta_value == 0:
        x0 = -b / (2 * a)
        return [x0]

    if delta_value < 0:
        x1 = (-b - sqrt(delta_value)) / (2 * a)
        x2 = (-b + sqrt(delta_value)) / (2 * a)
        return [x1, x2]

def formater_complexes(liste_complexes):
    resultat = []
    for z in liste_complexes:
        re = z.real  # Partie réelle
        im = z.imag  # Partie imaginaire

        # Si la partie imaginaire est nulle, n'afficher que la partie réelle
        if im == 0:
            resultat.append(f"{re:.2f}")
        # Sinon, afficher normalement
        elif im > 0:
            resultat.append(f"{re:.2f} + {abs(im):.2f}i")
        else:
            resultat.append(f"{re:.2f} - {abs(im):.2f}i")

    return resultat

# Demander les valeurs de a, b et c à l'utilisateur
a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))
c = float(input("Entrez la valeur de c : "))

# Calculer les solutions et les formater
solutions = formater_complexes(delta(a, b, c))

# Afficher le résultat
print(f"\nLes solutions de l'équation sont : {' et '.join(solutions)}.")
