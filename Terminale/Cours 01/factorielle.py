
def factorielle(n):
    if n == 0:  # Cas de base
        return 1
    else:
        return n * factorielle(n - 1)  # Cas récursif


n = int(input("Entrez la valeur de n : "))
print(factorielle(n))