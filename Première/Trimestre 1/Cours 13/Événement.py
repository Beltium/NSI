
"""Organisation d'un événement"""

# Décomposition :
#
#   Demander les informations de base sur l'événement (titre, date, lieu).
#   Permettre à l'utilisateur d'ajouter des invités un par un.
#   Afficher un récapitulatif de l'événement et la liste des invités.


# Informations de base sur l'événement
titre = input("Entrez le titre de l'événement : ")
date = input("Entrez la date de l'événement (JJ/MM/AAAA) : ")
lieu = input("Entrez le lieu de l'événement : ")

# Ajout des invités
invites = []
while True:
    invite = input("Entrez le nom d'un invité (ou 'fin' pour terminer) : ")
    if invite.lower() == 'fin':
        break
    invites.append(invite)

# Affichage du récapitulatif de l'événement
print("\nRésumé de l'événement :")
print(f"Titre : {titre}")
print(f"Date : {date}")
print(f"Lieu : {lieu}")
print("\nListe des invités :")
for invite in invites:
    print(f"- {invite}")

print(f"Nombre total d'invités : {len(invites)}")
