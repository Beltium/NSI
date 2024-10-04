
mangas = {}
while True:
    manga = input("Entrez le nom du manga (ou 'q' pour quitter) : ")
    if manga == 'q':
        break
    chapitres = int(input(f"Combien de chapitres avez-vous lus de {manga} ? "))

    avis = None
    avis_str = ""
    while avis_str not in ['y', 'n']:
        avis_str = input("Avez-vous aimé ? (y/n) : ").lower()
        if avis_str == 'y':
            avis = True
        elif avis_str == 'n':
            avis = False
        else:
            print("Vous devez répondre par 'y' (oui) ou 'n' (non).")

    mangas[manga] = (chapitres, avis)

    print("\nVous avez lu les chapitres suivants :")
    for manga, (chapitres, avis) in mangas.items():
        if avis:
            print(f"{manga} : {chapitres} chapitres --> Aimé")
        else:
            print(f"{manga} : {chapitres} chapitres --> Pas aimé")
