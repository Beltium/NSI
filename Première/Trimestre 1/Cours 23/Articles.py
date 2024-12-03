
articles = []

# Fonction print
def print_art(articles):
    if not articles: # Vérifier si il y a des articles
        print("Il n'y a pas encore d'articles.")
    else:
        for art in articles: # Les print un par un
            print(f"Titre: {art['titre']}, Auteur: {art['auteur']}, Date: {art['date']}\n")


# Fonction d'ajout d'articles
def add_art(titre, auteur, date, articles):
    article = {"titre": titre, "auteur": auteur, "date": date}
    articles.append(article)

# Fonction principale
def main():
    global articles # Mettre la liste 'articles' dans la fonction

    titre = "Élections américaines 2024"
    auteur = ("Jean Dupont")
    date = "03/12/2024"

    add_art(titre, auteur, date, articles)
    print_art(articles)



if __name__ == '__main__':
    main()