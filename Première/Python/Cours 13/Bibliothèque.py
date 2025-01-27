
"""Gestion d'une bibliothèque"""

# Décomposition :
#
#     Permettre à l'utilisateur d'ajouter un livre avec ses informations (titre, auteur, année).
#     Demander si l'utilisateur souhaite ajouter un autre livre ou terminer.
#     Afficher la liste complète des livres avec leurs informations.


# Initialisation de la bibliothèque
bibliotheque = []

# Ajout des livres
while True:
    titre = input("Entrez le titre du livre : ")
    auteur = input("Entrez l'auteur du livre : ")
    annee = input("Entrez l'année de publication du livre : ")

    # Ajout du livre sous forme de dictionnaire
    livre = {
        'titre': titre,
        'auteur': auteur,
        'annee': annee
    }
    bibliotheque.append(livre)

    # Demander si l'utilisateur souhaite ajouter un autre livre
    continuer = input("Voulez-vous ajouter un autre livre ? (oui/non) : ")
    if continuer.lower() != 'oui':
        break

# Affichage de la bibliothèque
print("\nListe des livres dans votre bibliothèque :")
for livre in bibliotheque:
    print(f"- {livre['titre']} de {livre['auteur']} (Publié en {livre['annee']})")

print(f"Nombre total de livres : {len(bibliotheque)}")
