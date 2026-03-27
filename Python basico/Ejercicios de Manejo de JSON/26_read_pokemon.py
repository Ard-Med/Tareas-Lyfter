
# Cree un programa que abra un archivo .json con la información de Pokémon y:
    # Lea el archivo JSON de Pokémon
    # Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

import json

def read_json (filename):
    with open(filename, encoding="utf-8") as file:
        data = json.load(file)
        for pokemon in data:
            print("Name: ", pokemon["name"]["english"])
            print("Type: ", pokemon["type"])
            print("Level: ", pokemon["level"])
            print("--------")

read_json("pokemon.json")