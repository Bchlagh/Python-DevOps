import os
import json

def parse_json(file_path):
    # Déterminer et afficher le chemin du fichier JSON
    print(f"Chemin du fichier JSON : {file_path}")

    # Créer un chemin absolu vers le fichier JSON
    abs_file_path = os.path.abspath(file_path)
    print(f"Chemin absolu du fichier JSON : {abs_file_path}")

    try:
        # Lire et analyser le fichier JSON
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

            # Extrait et affiche la valeur associée à la clé 'name'
            if 'name' in data:
                print(f"Valeur associée à la clé 'name' : {data['name']}")

            # Parcourt toutes les clés et valeurs du dictionnaire JSON
            print("Toutes les paires clé-valeur dans le fichier JSON:")
            for key, value in data.items():
                print(f"{key}: {value}")

    except FileNotFoundError:
        print("Le fichier JSON n'a pas été trouvé.")
    except json.JSONDecodeError:
        print("Erreur de décodage JSON. Assurez-vous que le fichier est au format JSON valide.")

if __name__ == "__main__":
    # Remplacez le chemin du fichier JSON par le chemin réel de votre fichier
    json_file_path = "chemin/vers/votre/fichier.json"
    parse_json(json_file_path)
