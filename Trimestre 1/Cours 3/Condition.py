
age = int(input("Quel est votre âge ? ")) # Saisie de l'âge

hasPhone = input("Avez vous un téléphone portable ? (y/n) ") # Demande si l'utilisateur possède un téléphone
if hasPhone == "y":
    hasPhone = True # Si oui, alors True
elif hasPhone == "n":
    hasPhone = False # Si non, alors False
else:
    print('Veuillez répondre avec "y" ou "n".') # Sinon, demande de ressaisir correctement
    exit()



if age < 13: # Conditions avec réponses simples
    if hasPhone:
        print("Vous êtes un enfant et ne devez pas avoir de téléphone portable si tôt.")
    else:
        print("Vous êtes un enfant.")

elif 13 <= age < 18: # Condition avec un encadrement
    if hasPhone:
        print("Vous êtes un adolescant et l'utilisation du téléphone et correcte.")
    else:
        print("Vous êtes un adolescent.")

elif age >= 18 and not hasPhone: # Double condition avec "and"
    print("Arrivez-vous à vivre ?")

else:
    print("Vous êtes un adulte.")