from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Charger les données
iris = load_iris()
X, y = iris.data, iris.target

# Séparer en ensemble d'entraînement (80%) et de test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser et entraîner le modèle k-NN avec k=3
modele = KNeighborsClassifier(n_neighbors=3)
modele.fit(X_train, y_train)

# Tester la précision du modèle
predictions = modele.predict(X_test)
precision = accuracy_score(y_test, predictions)
print("Précision du modèle :", precision)

# Définir une nouvelle fleur (modifie cette liste pour tester d'autres valeurs)
nouvelle_fleur = [5.1, 3.5, 1.4, 0.2]  # Longueur/Largeur sépale, Longueur/Largeur pétale

# Prédire l'espèce
prediction = modele.predict([nouvelle_fleur])[0]
print(f"L'espèce prédite est : {iris.target_names[prediction]}")
