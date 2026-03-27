# Cree un programa que me permita ingresar información de n cantidad de videojuegos y los guarde en un archivo csv.

import csv
import os

def get_game_info():
    name = input("Enter a game name: ")
    genre = input("Enter genre: ")
    developer = input("Enter developer: ")
    esrb = input("Enter ESRB rating: ")
    return {"Name" : name, "Genre" : genre, "Developer" : developer, "ESRB Rating" : esrb}


def game_headers ():
    game_headers = (
        "Name",
        "Genre",
        "Developer",
        "ESRB Rating"
    )
    return game_headers


def get_all_games ():
    games = []
    while True:
        games.append(get_game_info())
        finish = input("Enter another game? (Y/N): ")
        if finish.upper() == "N":
            break
    return games


def write_csv (filename, data, headers):
    file_exists = os.path.exists(filename)
    filecheck = "a" if file_exists else "w"
    with open(filename, filecheck, encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)


write_csv("videogames.csv", get_all_games(), game_headers())