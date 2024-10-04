
# Ce programme permet de calculer les n premiers termes de la suite de Fibonacci

n = int(input("Jusqu'à quel terme voulez-vous calculez la suite de Fibonacci ? "))
fibonacci = []

for i in range(n):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])


print(f"Voici les {n} premiers termes de la suite de Fibonacci : " + ', '.join(map(str, fibonacci)))