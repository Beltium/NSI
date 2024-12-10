
from write import file_path

f = open(file_path, 'r')

contenu = f.read()
f.close()
print(contenu)