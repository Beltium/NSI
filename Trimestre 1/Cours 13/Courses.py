# Initialisation de la liste des courses
courses = []

while True:
    produit = input("Entrez un produit à acheter (ou 'fin' pour terminer) : ")
    if produit.lower() == 'fin':
        break
    courses.append(produit)

# Affichage des courses
print("Liste de courses :")
for produit in courses:
    print("-", produit)
print(f"Nombre total d'articles : {len(courses)}")