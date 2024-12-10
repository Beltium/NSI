
file_path = "file.txt"

def write(str, file_path=file_path):
    try:
        with open(file_path, 'w') as f:
            f.write(str)
            f.close()
    except Exception as e:
        print(f"Erreur : {e}")

write("Hello World!\n"
      "Hello World 2!\n"
      "It's work !")
# write(2)