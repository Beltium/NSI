import math
import matplotlib.pyplot as plt
from collections import Counter

amis = [
    {"position": [1, 2], "sport": "Football"},
    {"position": [2, 3], "sport": "Football"},
    {"position": [3, 3], "sport": "Basketball"},
    {"position": [6, 6], "sport": "Basketball"},
    {"position": [5, 1], "sport": "Football"},
    {"position": [4, 2], "sport": "Basketball"},
    {"position": [7, 5], "sport": "Basketball"},
    {"position": [8, 3], "sport": "Football"},
    {"position": [2, 6], "sport": "Football"},
    {"position": [4, 5], "sport": "Basketball"}
]

nouveau_ami = [3, 5]

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Calcul des distances
distances = [(distance(ami["position"], nouveau_ami), ami["sport"], ami["position"]) for ami in amis]
k = 3
voisins_proches = sorted(distances)[:k]

# Classification
sports = [sport for _, sport, _ in voisins_proches]
sport_predi = Counter(sports).most_common(1)[0][0]
print("Sport préféré :", sport_predi)

# Couleurs pour les sports
couleurs = {"Football": "blue", "Basketball": "green"}

# Tracé des amis sans doublon dans la légende
labels_used = {"Football": False, "Basketball": False}
for ami in amis:
    sport = ami["sport"]
    label = sport if not labels_used[sport] else None  # Première occurrence seulement
    plt.scatter(*ami["position"], color=couleurs[sport], label=label, s=100)
    labels_used[sport] = True  # Marquer comme utilisé

# Tracé du nouveau venu
plt.scatter(*nouveau_ami, color="red", label="Nouveau", s=100, edgecolors="black")

# Encadrer les voisins proches
for _, _, pos in voisins_proches:
    plt.scatter(*pos, s=300, facecolors='none', edgecolors='black', linewidths=1.5)

plt.title("Visualisation de l'algorithme des k plus proches voisins (k-NN)")
plt.legend()
plt.grid()
plt.show()
