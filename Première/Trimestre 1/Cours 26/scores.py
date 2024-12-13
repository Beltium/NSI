
import json

file_path = "scores.json"

def write(dict, file_path=file_path):
    try:
        with open(file_path, 'w') as f:
            json.dump(dict, f, indent=5)
        print("Scores enregistrés avec succès !")
    except Exception as e:
        print(f"Erreur : {e}")

def read(file_path=file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
        print("Scores chargés avec succès !")
    except Exception as e:
        return {}
        print(f"Erreur : {e}")

def main():
    scores = read()
    while True:
        name = input("Entrez le nom du joueur : ")
        score, total = 0, []
        while True:
            score = input(f"Entrez un score pour {name} ('fin' pour terminer) : ")
            if score == 'fin':
                break
            total.append(int(score))
        scores[name] = total
        print(scores)



if __name__ == '__main__':
    main()