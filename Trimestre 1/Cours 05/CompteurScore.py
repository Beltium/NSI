
total_points = 0

while True:
    points = int(input("Entrez les points gagnés (0 pour terminer) : "))
    if points == 0:
        break
    total_points += points
    print("Le score total est :", total_points)