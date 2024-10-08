
# Ce programme permet de calculer les n premiers termes de la suite de Fibonacci

n = int(input("Jusqu'à quel terme voulez-vous calculer la suite de Fibonacci ? "))

def fibonacci(n):
    fibonacci = []

    for i in range(n):
        if i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci


print(f"Voici les {n} premiers termes de la suite de Fibonacci : " + ', '.join(map(str, fibonacci(n))))