import random, math

rg = 100

sections = list(range(1, rg+1))
section_tresor = random.choice(sections)


def recherche_binaire(liste, debut, fin, cible, tentatives=math.ceil(math.log2(rg))):
    if debut > fin or tentatives == 0:
        print("Le trésor n'a pas été trouvé, vous avez épuisé vos tentatives.")
        return -1

    milieu = (debut + fin) // 2
    print(f"Vous cherchez dans la section {milieu}... Tentatives restantes : {tentatives}")

    if liste[milieu] == cible:
        print(f"Félicitations ! Vous avez trouvé le trésor dans la section {milieu} !")
        return milieu
    elif liste[milieu] < cible:
        print("Le trésor est dans une section plus haute.")
        return recherche_binaire(liste, milieu + 1, fin, cible, tentatives - 1)
    else:
        print("Le trésor est dans une section plus basse.")
        return recherche_binaire(liste, debut, milieu - 1, cible, tentatives - 1)


# Appel de la fonction
recherche_binaire(sections, 0, len(sections) - 1, section_tresor)