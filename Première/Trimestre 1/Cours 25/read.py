
from write import file_path

def read(file_path=file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Erreur : {e}")

contenu = read()
print(contenu)