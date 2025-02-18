# fetch_pokemon.py
import requests
import sys

def get_pokemon_abilities(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Error: Unable to fetch data for {pokemon_name}"
    
    data = response.json()
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    return abilities