
"""Calculateur d'IMC"""

def calculer_imc(poids, taille):
    return poids / (taille ** 2)

poids = float(input("Entrez votre poids en kg : "))
taille = float(input("Entrez votre taille en mètres : "))
imc = calculer_imc(poids, taille)

print(f"Votre IMC est : {imc:.2f}")

if imc < 18.5:
    print("Vous êtes en sous-poids.")
elif 18.5 <= imc < 25:
    print("Vous avez un poids normal.")
else:
    print("Vous êtes en surpoids.")
