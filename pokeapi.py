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

def get_pokemon_info(pokemon):
    """
    Fetches information for a specified Pokémon from the PokéAPI.

    Parameters:
        pokemon (str or int): Pokémon name or PokéDex number.

    Returns:
        dict: Pokémon data if successful.
        None: If the Pokémon is not found.
    """
    pokemon = str(pokemon).strip().lower()
    print(f"Fetching data for Pokémon: {pokemon}...")

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Pokémon data retrieved successfully!")
        return response.json()
    else:
        print(f"Error: Pokémon '{pokemon}' not found.")
        return None
