import json

# Chemin du fichier pour enregistrer les scores
file_path = "scores.json"

def write(scores, file_path=file_path):
    """Enregistre les scores dans un fichier JSON."""
    try:
        with open(file_path, 'w') as f:
            json.dump(scores, f, indent=5)
        print("Scores enregistrés avec succès !")
    except Exception as e:
        print(f"Erreur lors de l'enregistrement : {e}")

def read(file_path=file_path):
    """Charge les scores depuis un fichier JSON."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Fichier non trouvé. Un nouveau fichier sera créé.")
        return {}
    except Exception as e:
        print(f"Erreur lors de la lecture : {e}")
        return {}

def afficher_meilleur_score(scores):
    """Affiche le meilleur score et le joueur associé."""
    meilleur_score = 0
    meilleur_joueur = ""

    for joueur, scores_joueur in scores.items():
        score_max = max(scores_joueur, default=0)
        if score_max > meilleur_score:
            meilleur_score = score_max
            meilleur_joueur = joueur

    if meilleur_joueur:
        print(f"Le meilleur joueur est {meilleur_joueur} avec un score de {meilleur_score}.")
    else:
        print("Aucun score enregistré.")

def main():
    scores = read()

    while True:
        print("\nMenu :")
        print("1. Ajouter des scores")
        print("2. Afficher les scores")
        print("3. Afficher le meilleur score")
        print("4. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            # Ajouter des scores
            while True:
                nom = input("Entrez le nom du joueur (ou 'fin' pour revenir au menu) : ")
                if nom.lower() == "fin":
                    break

                if nom not in scores:
                    scores[nom] = []

                while True:
                    score = input(f"Entrez un score pour {nom} ('fin' pour arrêter) : ")
                    if score.lower() == "fin":
                        break
                    try:
                        scores[nom].append(int(score))
                    except ValueError:
                        print("Veuillez entrer un nombre valide.")

            write(scores)

        elif choix == "2":
            # Afficher les scores
            print("\nScores enregistrés :")
            for joueur, scores_joueur in scores.items():
                print(f"{joueur} : {', '.join(map(str, scores_joueur))}")

        elif choix == "3":
            # Afficher le meilleur score
            afficher_meilleur_score(scores)

        elif choix == "4":
            # Quitter le programme
            print("Au revoir !")
            break

        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == '__main__':
    main()
