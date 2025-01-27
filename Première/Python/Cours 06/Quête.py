
def choix_action():
    print("\nQue voulez-vous faire ?")
    print("1. Explorer la forêt")
    print("2. Entrer dans la ville")
    print("0. Quitter la quête")
    return input("Entrez votre choix (1/2/0) : ")

def explorer_forets():
    print("Vous explorez la forêt et trouvez un trésor !")
    print("Vous avez gagné 100 pièces d'or.")

def entrer_ville():
    print("Vous entrez dans la ville et rencontrez un villageois.")
    print("Il vous donne des informations sur une quête cachée.")

    choix = ""
    while choix not in ["y", "n"]:
        choix = input("\nVoulez-vous suivre ses instrcutions pour accèdes à la quête cachée ? (y/n) ")
        if choix == "y":
            print("Vous suivez un chemin et vous vous faites attaquer.")
            print("Vous n'arrivez pas à vous battre, ils sont trop nombreux.")
            print("Vous mourrez...")

        elif choix == "n":
            print("Vous apprenez le lendemain qu'un aventurier à suivi la quête cachée et s'est fait tuer.")
            print("Vous avez donc bien fait de ne pas y être allé.")

        else:
            print("Vous devez répondre par 'y' (oui) ou 'n' (non).")


def main():
    while True:
        choix = choix_action()
        if choix == "1":
            explorer_forets()

        elif choix == "2":
            entrer_ville()

        elif choix == "0":
            print("Merci d'avoir joué !")
            break

        else:
            print("Choix invalide. Essayez encore.")


# Exécution du programme principal
if __name__ == '__main__':
    main()