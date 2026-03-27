# Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON.

import json

def read_json (filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def get_pokemon_info():
    name = input("Enter a pokemon name: ")
    level = int(input("Enter level: "))
    pokemon_type = [t.strip() for t in input("Enter the type(s), separated by a comma: ").split(",")]
    hp = int(input("Enter HP value: "))
    attack = int(input("Enter attack value: "))
    defense = int(input("Enter defense value: "))
    sp_attack = int(input("Enter special attack value: "))
    sp_defense = int(input("Enter special defense value: "))
    speed = int(input("Enter speed value: "))
    return {"name": {"english" : name},
            "level" : level,
            "type" : pokemon_type, 
            "base" : {  
                "HP" : hp,
                "Attack" : attack,
                "Defense" :defense,
                "Sp. Attack" : sp_attack,
                "Sp. Defense" : sp_defense,
                "Speed" : speed
                }
            }


def append_json (filename, new_pokemon):
    data = read_json(filename)
    data.append(new_pokemon)
    with open(filename,"w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


append_json("pokemon.json", get_pokemon_info())