import requests
import random


def get_random_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1"
    response = requests.get(url)
    if response.status_code != 200:
        return "Couldn't fetch pokemon, try again"
    data = response.json()

    # total_pokemon = data["count"]

    random_id = random.randint(1, 1000)

    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
    pokemon_response = requests.get(pokemon_url)
    pokemon_data = pokemon_response.json()

    return pokemon_data


def get_sprite():
    pokemon_data = get_random_pokemon()

    sprites = pokemon_data["sprites"]
    sprites_other = sprites["other"]
    sprites_home = sprites_other["home"]

    return sprites_home


def get_name():
    pokemon_data = get_random_pokemon()

    pokemon_name = pokemon_data["name"]

    return pokemon_name
