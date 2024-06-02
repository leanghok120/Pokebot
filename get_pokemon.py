import requests
import random

url = "https://pokeapi.co/api/v2/pokemon?limit=1"
response = requests.get(url)
data = response.json()


def get_random_pokemon():
    total_pokemon = data["count"]

    random_id = random.randint(1, total_pokemon)

    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
    pokemon_response = requests.get(pokemon_url)
    pokemon_data = pokemon_response.json()

    return pokemon_data


pokemon_data = get_random_pokemon()


def get_sprite():
    sprites = pokemon_data["sprites"]
    sprites_other = sprites["other"]
    sprites_home = sprites_other["home"]

    return sprites_home


def get_name():
    pokemon_name = pokemon_data["name"]

    return pokemon_name
