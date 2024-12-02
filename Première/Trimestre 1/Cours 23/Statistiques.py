
import statistics as stat


def calcul_statistiques(data):
    etendue = max(data) - min(data)
    moyenne = stat.mean(data)
    median = stat.median(data)
    ecart_type = stat.stdev(data) if len(data) > 1 else 0
    return (etendue, moyenne, median, ecart_type)

données = input("Entrez vos valeurs (séparées par des virgules) : ").split(", ")
données = [float(val) for val in données]

etendue, moyenne, median, ecart_type = calcul_statistiques(données)

print(f"\nL'étendue est de {etendue:.2f}.")
print(f"La moyenne est de {moyenne:.2f}.")
print(f"La médianne est de {median:.2f}.")
print(f"L'écart type est de {ecart_type:.2f}.")