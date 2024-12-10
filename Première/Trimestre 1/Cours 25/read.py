
# Récupérer le file_path depuis write.py
from write import file_path

# Fonction de lecture
def read(file_path=file_path):
    try:
        with open(file_path, 'r') as f:
            # On retourne directement ce qui est lu
            return f.read()
    except Exception as e:
        # Gestion des erreurs identiques à write.py
        print(f"Erreur : {e}")

# Petit test
contenu = read()
print(contenu)