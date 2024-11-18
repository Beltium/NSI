liste = []

liste.append(5)
print(liste)

liste.append(10)
print(liste)

liste.insert(1, 7)
print(liste)

liste.remove(7)
print(liste)

element = liste.pop(1)
print(element, liste)

existe = 10 in liste
print(existe)

longueur = len(liste)
print(longueur)