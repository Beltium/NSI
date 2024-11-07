import random, math
import matplotlib.pyplot as plt

# Variables
rg = 1000
sections = list(range(1, rg + 1))
section_tresor = random.choice(sections)


def recherche_binaire(liste, debut, fin, cible, tentatives=math.ceil(math.log2(rg))):
    plt.ion()  # Mode interactif pour matplotlib
    fig, ax = plt.subplots()
    ax.set_xlim(0, rg)
    ax.set_ylim(0, 1)
    ax.get_yaxis().set_visible(False)

    # Boucle de recherche
    while debut <= fin and tentatives > 0:
        milieu = (debut + fin) // 2


        ax.clear()

        ax.plot(sections, [0.5] * rg, 's', color="lightgrey", markersize=10, label="Sections")

        ax.plot(cible, 0.5, 's', color="gold", markersize=12, label="Trésor")

        ax.plot(liste[milieu], 0.5, 's', color="blue", markersize=12, label="Recherche actuelle")

        ax.set_title(f"Vous cherchez dans la section {milieu + 1}... Tentatives restantes : {tentatives}")

        # Légende
        ax.legend(loc="upper right")
        plt.draw()
        plt.pause(1)

        if liste[milieu] == cible:
            print(f"Félicitations ! Vous avez trouvé le trésor dans la section {milieu + 1} !")
            plt.title("Trésor trouvé !")
            plt.show(block=True)
            return milieu
        elif liste[milieu] < cible:
            print("Le trésor est dans une section plus haute.")
            debut = milieu + 1
        else:
            print("Le trésor est dans une section plus basse.")
            fin = milieu - 1

        tentatives -= 1

    print("Le trésor n'a pas été trouvé, vous avez épuisé vos tentatives.")
    plt.title("Trésor non trouvé, tentatives épuisées.")
    plt.show(block=True)
    return -1


# Appel de la fonction
recherche_binaire(sections, 0, len(sections) - 1, section_tresor)
