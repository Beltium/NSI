
# Initiation des personnages
characters = {}

def add_character():
    while True:
        name = input("Entrez le nom du personnage : ")

        try :
            age = int(input(f"Entrez l'age de {name} : "))
        except ValueError:
            print("Erreur : Veuillez entrez une valeur numérique pour l'âge.")
            continue

        role = input(f"Entrez le rôle de {name} : ")
        skills = input(f"Entrez les compétences de {name} (séparé par des virgules) : ").split(", ")

        inventory = {}
        while True:
            item = input("Entrez un objet à rajouter à l'inventaire : ")
            if item.lower() == 'fin':
                break
            try:
                quantity = int(input(f"Combien de {item} faut-il ajouter ? "))
            except ValueError:
                print("Erreur : Veuillez entrz une valeur numérique pour la quantité.")
                continue
            inventory[item] = quantity

        characters[name] = {
            "age": age,
            "role": role,
            "skills": tuple(skills),
            "inventory": inventory
        }
        print(f"{name} a été ajouté avec succés.")