import requests
import random


def get_sprite():

    url = "https://pokeapi.co/api/v2/pokemon?limit=1"
    response = requests.get(url)
    data = response.json()

    total_pokemon = data["count"]

    random_id = random.randint(1, total_pokemon)

    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
    pokemon_response = requests.get(pokemon_url)
    pokemon_data = pokemon_response.json()

    # Sprites
    sprites = pokemon_data["sprites"]
    sprites_other = sprites["other"]
    sprites_home = sprites_other["home"]

    return sprites_home
