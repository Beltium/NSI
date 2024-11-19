import numpy as np
import matplotlib.pyplot as plt

# Définir la fonction de Gauss
def gauss_function(x):
    return np.exp(-x**2)

x = np.linspace(-3, 3, 500)
y = gauss_function(x)

# Tracé
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='$f(x) = e^{-x^2}$', color='blue')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title("Fonction de Gauss $f(x) = e^{-x^2}$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.legend()
plt.show()
