
liste = (
    ['pommes', 'lait', 'œufs'],
    ['pain', 'fromage', 'beurre']
         )

choix = int(input("Quelle liste voulez-vous voir ? (1 ou 2) : ")) - 1
print(", ".join(liste[choix]))
