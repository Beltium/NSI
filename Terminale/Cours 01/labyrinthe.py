def explorer_labyrinthe(labyrinthe, x, y, visitees):
    # Vérifier les limites du labyrinthe
    if x < 0 or x >= len(labyrinthe) or y < 0 or y >= len(labyrinthe[0]):
        return False

    # Vérifier si la case est un mur ou déjà visitée
    if labyrinthe[x][y] == 1 or (x, y) in visitees:
        return False

    # Si on a trouvé la sortie
    if labyrinthe[x][y] == 'E':
        print(f"Sortie trouvée à la position ({x}, {y})")
        return True

    # Marquer la case comme visitée
    visitees.add((x, y))

    # Appeler la fonction récursive dans les 4 directions
    if (explorer_labyrinthe(labyrinthe, x + 1, y, visitees) or  # Bas
            explorer_labyrinthe(labyrinthe, x - 1, y, visitees) or  # Haut
            explorer_labyrinthe(labyrinthe, x, y + 1, visitees) or  # Droite
            explorer_labyrinthe(labyrinthe, x, y - 1, visitees)):  # Gauche
        return True

    # Si aucune direction ne fonctionne, on retourne False
    return False



labyrinthe = [
    ['S', 1  , 0  , 0  , 1],
    [0  , 1  , 0  , 1  , 0],
    [0  , 0  , 0  , 1  , 'E'],
    [1  , 1  , 0  , 0  , 0],
    [0  , 0  , 0  , 1  , 0]
]

# Position de départ (0, 0)
position_depart = (0, 0)

# Ensemble des cases visitées
cases_visitees = set()

# Lancer la recherche de la sortie
explorer_labyrinthe(labyrinthe, position_depart[0], position_depart[1], cases_visitees)
