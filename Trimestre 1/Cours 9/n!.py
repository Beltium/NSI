
"""Calculateur de n factoriel (n!)"""

def factoriel(n):
    if n == 0:
        return 1
    else:
        return n * factoriel(n-1)


n = int(input("De quel nombre voulez-vous calculer le factoriel ? "))
print(factoriel(n))