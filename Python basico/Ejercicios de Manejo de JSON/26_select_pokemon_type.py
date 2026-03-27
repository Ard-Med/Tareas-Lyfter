# Cree un programa que abra un archivo .json con la información de Pokémon y:
    # Lea el archivo JSON de Pokémon
    # Pida al usuario un tipo de Pokémon
    # Muestre todos los Pokémon que sean de ese tipo

import json

def read_json (filename):
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
        pokemon_type = input("Enter a pokemon type: ")
        for pokemon in data:
            if pokemon_type in pokemon["type"]:
                print(json.dumps(pokemon, indent=2))

read_json("pokemon.json")