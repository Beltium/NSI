# Initialisation de la liste pour stocker les cas de chaque jour
cas_covid = []

# Saisie des cas pour chaque jour de la semaine (7 jours)
for jour in range(7):
    while True:
        try:
            cas = int(input(f"Entrez le nombre de cas pour le jour {jour + 1} : "))
            if cas < 0:
                print("Le nombre de cas ne peut pas être négatif, veuillez réessayer.")
            else:
                cas_covid.append(cas)
                break
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

# Calcul de la somme totale des cas sur la semaine
total_cas = sum(cas_covid)
print(f"\nNombre total de cas sur la semaine : {total_cas}")

# Calcul de la moyenne des cas par jour
moyenne_cas = total_cas / len(cas_covid)
print(f"Moyenne de cas par jour : {moyenne_cas:.2f}")

# Identification du jour avec le plus grand nombre de cas
jour_max_cas = cas_covid.index(max(cas_covid)) + 1
print(f"Le jour avec le plus grand nombre de cas est le jour {jour_max_cas} avec {max(cas_covid)} cas.\n")

# Analyse quotidienne : comparaison des cas d'un jour à l'autre
for jour in range(1, len(cas_covid)):
    if cas_covid[jour] > cas_covid[jour - 1]:
        print(f"Le jour {jour + 1}, les cas ont augmenté par rapport au jour précédent.")
    elif cas_covid[jour] < cas_covid[jour - 1]:
        print(f"Le jour {jour + 1}, les cas ont diminué par rapport au jour précédent.")
    else:
        print(f"Le jour {jour + 1}, le nombre de cas est resté identique.")

# Nouvelle fonctionnalité : Calcul et affichage des jours avec des cas au-dessus de la moyenne
jours_au_dessus_moyenne = [i + 1 for i, cas in enumerate(cas_covid) if cas > moyenne_cas]
print(f"\nNombre de jours avec un nombre de cas supérieur à la moyenne ({moyenne_cas:.2f}) : {len(jours_au_dessus_moyenne)}")

if jours_au_dessus_moyenne:
    print("Ces jours sont :", ', '.join(map(str, jours_au_dessus_moyenne)))
else:
    print("Aucun jour n'a eu un nombre de cas supérieur à la moyenne.")
