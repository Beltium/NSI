def attaque_bonus(n, critique=False):
    if n == 0:
        return 0
    else:
        bonus = (10 - n)  # Le bonus diminue avec chaque coup
        if critique and n % 5 == 0:
            bonus *= 3  # Coup critique tous les 3 coups
        return bonus + attaque_bonus(n - 1, critique)


# Exemple d'utilisation :
for i in [3, 5, 10]:
    print(f"Pour {i} coups :")
    total_bonus = attaque_bonus(i, critique=True)
    print(f"Le total des points d'attaque avec coups critiques est de : {total_bonus}\n")