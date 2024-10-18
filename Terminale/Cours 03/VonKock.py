import turtle

def von_koch(longueur, niveau):
    if niveau == 0:
        turtle.forward(longueur)
    else:
        longueur /= 3
        von_koch(longueur, niveau - 1)
        turtle.left(60)
        von_koch(longueur, niveau - 1)
        turtle.right(120)
        von_koch(longueur, niveau - 1)
        turtle.left(60)
        von_koch(longueur, niveau - 1)

# Fonction pour dessiner le flocon de Von Koch complet
def flocon_von_koch(longueur, niveau):
    for _ in range(3):
        von_koch(longueur, niveau)
        turtle.right(120)

# Initialisation de Turtle
turtle.speed("fastest")
turtle.penup()
turtle.goto(-200, 100)  # Position initiale pour centrer le flocon
turtle.pendown()

# Appel de la fonction pour dessiner le flocon de Von Koch
flocon_von_koch(400, 4)  # Longueur de 400 et 4 niveaux de récursivité

# Finalisation du dessin
turtle.done()
