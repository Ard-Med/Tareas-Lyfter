# Cree un programa que abra un archivo .json con la información de Pokémon y:
# Lea el archivo JSON de Pokémon
# Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)

import json

def read_json (filename):
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
        for pokemon in data:
            print (pokemon["name"]["english"])
            for stat, value in pokemon["base"].items():
                print(f"{stat}:{value}")
            print("-----")

read_json("pokemon.json")