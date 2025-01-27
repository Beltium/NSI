# Initialisation du dictionnaire pour un personnage
personnage = {}

# Demander les informations sur le personnage
personnage["nom"] = input("Entrez le nom du personnage : ")
personnage["age"] = int(input("Entrez l'âge du personnage : "))
personnage["vie"] = int(input("Entrez les points de vie du personnage : "))
personnage["niveau"] = int(input("Entrez le niveau du personnage : "))
personnage["inventaire"] = input("Entrez les items de son inventaire (séparés par une virgule) : ").split(", ")
personnage["réel"] = True if input("Le personnage est-il réelle ? (y/n) ").lower() == "y" else False

# Afficher les informations du personnage
print("\nInformations du personnage :")
print(f"Nom : {personnage['nom']}")
print(f"Âge : {personnage['age']}")
print(f"Points de vie : {personnage['vie']}")
print(f"Niveau : {personnage['niveau']}")
print(f"Inventaire : {", ".join(personnage["inventaire"])}")
print("Le personnage est", "réel." if personnage["réel"] else "fictif.")

# Modifier les points de vie et le niveau
personnage["vie"] = int(input("\nEntrez les nouveaux points de vie : "))
personnage["niveau"] = int(input("Entrez le nouveau niveau : "))

# Afficher les informations mises à jour
print("\nInformations mises à jour :")
print(f"Nom : {personnage['nom']}")
print(f"Points de vie : {personnage['vie']}")
print(f"Niveau : {personnage['niveau']}")