import time


# Fonction de recherche linéaire
def recherche_lineaire(liste, cible):
    for i in range(len(liste)):
        print(f"Vérification de la section {liste[i]}")
        if liste[i] == cible:
            print(f"Objet trouvé dans la section {liste[i]}")
            return i
    print("Objet non trouvé")
    return -1


# Fonction de recherche binaire
def recherche_binaire(liste, debut, fin, cible):
    if debut > fin:
        print("Objet non trouvé")
        return -1

    milieu = (debut + fin) // 2
    print(f"Vérification de la section {liste[milieu]}...")

    if liste[milieu] == cible:
        print(f"Objet trouvé dans la section {liste[milieu]}")
        return milieu
    elif liste[milieu] < cible:
        return recherche_binaire(liste, milieu + 1, fin, cible)
    else:
        return recherche_binaire(liste, debut, milieu - 1, cible)


# Liste de 10 000 sections
sections = list(range(1, 100001))

# Chronométrer la recherche linéaire
print("=== Recherche Linéaire ===")
start_time = time.time()
recherche_lineaire(sections, 100000)
lin_time = time.time() - start_time
print(f"Temps d'exécution de la recherche linéaire : {lin_time:.6f} secondes\n")

# Chronométrer la recherche binaire
print("=== Recherche Binaire ===")
start_time = time.time()
recherche_binaire(sections, 0, len(sections) - 1, 100000)
bin_time = time.time() - start_time
print(f"Temps d'exécution de la recherche binaire : {bin_time:.6f} secondes\n")

# Comparaison des performances
print(f"Résumé :\nRecherche Linéaire : {lin_time:.6f} secondes\nRecherche Binaire : {bin_time:.6f} secondes")
