
# Définir le chemin du fichier
file_path = "file.txt"

# Fonction d'écriture
def write(str, file_path=file_path):
    try:
        with open(file_path, 'w') as f: # Équivalent de f = open()
            f.write(str)
            f.close()
    except Exception as e:
        # Gestion des erreurs : afficher simplement l'erreur
        print(f"Erreur : {e}")

write("Hello World!\n"
      "Hello World 2!\n"
      "It's work !")
# write(2)
# Test de gestion des erreurs : un int ne peut pas être écrit sans être transformé en str avant