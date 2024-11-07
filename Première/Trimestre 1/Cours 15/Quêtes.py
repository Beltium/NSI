from time import sleep

for i in range(3):  # Répéter la quête trois fois
    print("Choisissez une quête :")
    print("1. Explorer la forêt")
    print("2. Entrer dans la ville")

    choix = input("Entrez votre choix (1/2) : ")

    if choix == "1":
        print("Chargement de la quète...")
        for n in range(101):
            print(f"\r{n}%", end="")  # \r pour réécrire la ligne et end="" pour rester sur la même ligne
            sleep(0.1)
        print("\nVous explorez la forêt et trouvez un trésor !")
    elif choix == "2":
        print("Vous entrez dans la ville et rencontrez un marchand.")
    else:
        print("Choix invalide.")