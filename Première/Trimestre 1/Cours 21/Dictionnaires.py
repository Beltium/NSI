personnage = {
    "nom": "Naruto",
    "age": 16,
    "niveau": 5
    }

print(personnage["nom"])  # Affiche "Naruto"

personnage["vie"] = 100  # Ajoute une nouvelle clé "vie" avec une valeur de 100
personnage["niveau"] = 6  # Modifie la valeur de "niveau" à 6

print(personnage)

del personnage["age"]  # Supprime la clé "age"

if "vie" in personnage:
            print("Le personnage a des points de vie.")