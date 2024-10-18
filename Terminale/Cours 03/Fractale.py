import turtle


def dessiner_arbre(longueur, angle):
    if longueur > 5:
        turtle.forward(longueur)
        turtle.right(angle)
        dessiner_arbre(longueur - 15, angle)
        turtle.left(angle * 2)
        dessiner_arbre(longueur - 15, angle)
        turtle.right(angle)
        turtle.backward(longueur)


# Initialisation de Turtle
turtle.speed("fastest")
turtle.left(90)  # Faire pointer la tortue vers le haut
turtle.goto(0, -100)
dessiner_arbre(100, 15)  # Commence avec une longueur de 100
turtle.done()