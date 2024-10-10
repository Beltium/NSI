
consommation_moyenne = 0

def readFiles():
    donnés = {}
    for fichier_nom in ['conso1.txt', 'conso2.txt']:
        try:
            # Tenter d'ouvrir le fichier et de lire les lignes
            with open(fichier_nom, 'r') as fichier:
                lignes_lues = fichier.readlines()

            # Supprimer les sauts de ligne avec strip() pour chaque ligne
            donnés[fichier_nom] = [ligne.strip() for ligne in lignes_lues]


        except FileNotFoundError:
            # Ce qui arrive si le fichier n'existe pas
            print(f"Erreur : Le fichier '{fichier_nom}' n'existe pas.")

    print("Donnés lues avec succès.")
    return donnés

def calculCouts(n):
    global donnés, consommation_moyenne

    distance_totale = 0
    total_essence = 0

    if n == 1:
        consommation_moyenne = float(donnés['conso1.txt'][1])
        nom_véhicule = str(donnés['conso1.txt'][0])
    elif n == 2:
        consommation_moyenne = float(donnés['conso2.txt'][1])
        nom_véhicule = str(donnés['conso2.txt'][0])

    print(f"\nLe véhicule {n} est une {nom_véhicule} qui consomme {consommation_moyenne} L/100km.")
    while True:

        # Demander la distance parcourue pour un trajet
        distance = float(input("Entrez la distance parcourue lors de ce trajet (km, 0 pour terminer) : "))

        if distance == 0:  # Si la distance est 0, la simulation se termine
            break

        # Calculer la consommation d'essence pour ce trajet
        essence_utilisee = (distance / 100) * consommation_moyenne

        # Ajouter la consommation et la distance au total
        total_essence += essence_utilisee
        distance_totale += distance

        # Afficher la consommation pour ce trajet
        print(f"Essence consommée pour ce trajet : {essence_utilisee:.2f} litres")

    # Afficher la consommation totale et la distance totale à la fin
    print(f"\nDistance totale parcourue : {distance_totale} km")
    print(f"Essence totale consommée : {total_essence:.2f} litres")

def enregistrerConso():
    voiture = 0
    while voiture not in ["1", "2"]:
        voiture = input("Pour quelle voiture voulez-vous enregistrer la consommation moyenne ? (1/2) ")

        if voiture == "1":
            nom_voiture1 = input("Entrez le nom du véhicule : ")
            consommation_moyenne1 = str(input("Entrez la consommation moyenne du véhicule (L/100km) : "))
            info1 = [nom_voiture1, consommation_moyenne1]

            lignes_a_ecrire = [element + "\n" for element in info1]
            with open('conso1.txt', 'w') as fichier:
                fichier.writelines(lignes_a_ecrire)

            print(f'Enregistrement du véhicule "{nom_voiture1}" qui consomme {consommation_moyenne1} L/100km.')

        elif voiture == "2":
            nom_voiture2 = input("Entrez le nom du véhicule : ")
            consommation_moyenne2 = str(input("Entrez la consommation moyenne du véhicule (L/100km) : "))
            info1 = [nom_voiture2, consommation_moyenne2]

            lignes_a_ecrire = [element + "\n" for element in info1]
            with open('conso2.txt', 'w') as fichier:
                fichier.writelines(lignes_a_ecrire)

            print(f'Enregistrement du véhicule "{nom_voiture2}" qui consomme {consommation_moyenne2} L/100km.')

        else:
            print("Veuillez répondre correctement.")




while True:
    donnés = readFiles()
    print("\nCalculateur de coûts d'essence.")
    print("1. Utiliser la véhicule 1.")
    print("2. Utiliser le véhicule 2")
    print("3. Modifier la consommation d'une véhicule.")
    choix = input("Que voulez-vous faire ? (1/2/3) ? ")

    if choix == "1":
        calculCouts(1)

    elif choix == "2":
        calculCouts(2)

    elif choix == "3":
        enregistrerConso()

    else:
        print("Veuillez répondre correctement.")