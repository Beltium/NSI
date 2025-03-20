import math
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

nouveau_ami = [3, 4]

def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Calcul des distances entre le nouveau venu et chaque ami
distances = [(distance(ami["position"], nouveau_ami), ami["sport"]) for ami in amis]
print(distances)

k = 3
voisins_proches = sorted(distances)[:k]
print(voisins_proches)

# Détermination du sport le plus fréquent parmi les k voisins
sports = [sport for _, sport in voisins_proches]
sport_predi = Counter(sports).most_common(1)[0][0]

print("Sport préféré :", sport_predi)
