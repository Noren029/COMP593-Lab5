'''log_matching.py - Module to help analyze a log file using regular expressions.
COMP 593 Scripting Applications - Winter 2025 (Week 5)
Louis Bertrand <louis.bertrand@flemingcollege.ca>

Usage: Import this module into your main program

### STUDENTS: PLEASE ADD THE STANDARD ACADEMIC INTEGRITY STATEMENT.###
# This program is strictly my own work. Any material beyond course learning
# materials that is taken from the Web or other sources is properly cited,
# giving credit to the original author(s).

'''
import requests
import sys

def get_pokemon_abilities(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Invalid Pokémon name or API issue.")
        sys.exit(1)
    data = response.json()
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    return abilities
