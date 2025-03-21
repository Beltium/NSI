
# Import des modules
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

# Prédire sur les données de test et évaluer la précision
predictions = modele.predict(X_test)
precision = accuracy_score(y_test, predictions)

print("Prédictions :", predictions)
print(f"Précision du modèle : {precision*100}%")
