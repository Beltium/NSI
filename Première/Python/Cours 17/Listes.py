
from time import sleep

liste = []

while True:

    obj = input("Entrez un article (ou 'fin' pour arrêter) : ")

    if obj.lower() == 'fin':
        break
    else:
        liste.append(obj.lower())

print("Votre liste contient : ", ", ".join(liste))

if len(liste) > 1:
    sleep(0.2)

    print("\nSuppression des 2 derniers éléments...")
    liste = liste[:-2]
    sleep(2)
    print("Votre liste contient : ", ", ".join(liste))
