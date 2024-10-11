
def main():
    name = input("Quel est votre nom ? ")  # Demande le nom du joueur
    score = input("Entrez votre score : ") # Demande le score du joueur

    try:
        diff_score = 1000 - int(score) # Calcule la différence pour atteindre 1000pts

        if diff_score <= 0: # Si le score est inférieur ou égal à 0pts
            print(f"{name} a {int(score)} points et gagne !") # Alors il gagne et on affiche un message dans la console
        else:
            print(f"{name} a {int(score)} point(s) et il lui en manque {diff_score} pour gagner !") # Sinon, il lui indique combien de pts il nlui manque


    except ValueError: # Si l'utilisateur n'a pas rentré un nombre dans la variable score, un message d'erreur s'affiche
        print("Vous devez rentrer un nombre comme score !")


    fav_game = input("\nQuel est votre jeu préféré ? ") # Demande le jeu favori

    if fav_game != "Outer Wilds": # Si ce n'est pas Outer Wilds
        print("C'est faux ! Votre jeu favori est Outer Wilds et si ce n'est pas le cas, c'est que vous n'y avez pas encore joué ;(.") # Alors, un message est envoyé dans la console
    else:
        print("Je suis tout à fait d'accord, Outer Wilds est le meilleur jeu :).") # Sinon, un autre message est envoyé


if __name__ == '__main__':
    main() # Éxécution de la fonction principale main()