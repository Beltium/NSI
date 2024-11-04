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

def flocon_von_koch(longueur, niveau):
    for _ in range(3):
        von_koch(longueur, niveau)
        turtle.right(120)

turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()

flocon_von_koch(400, 4)
turtle.done()