'''log_matching.py - Module to help analyze a log file using regular expressions.
COMP 593 Scripting Applications - Winter 2025 (Week 5)
Louis Bertrand <louis.bertrand@flemingcollege.ca>

Usage: Import this module into your main program

### STUDENTS: PLEASE ADD THE STANDARD ACADEMIC INTEGRITY STATEMENT.###
# This program is strictly my own work. Any material beyond course learning
# materials that is taken from the Web or other sources is properly cited,
# giving credit to the original author(s).

'''

import sys
from pokeapi import get_pokemon_info
from pastebinapi import create_paste

def get_pokemon_name():
    """
    Gets the Pokémon name from command-line arguments.

    Returns:
        str: Pokémon name.

    Exits:
        Prints an error and exits if no name is provided.
    """
    if len(sys.argv) != 2:
        print("Error: Please provide a Pokémon name.")
        print("Usage: python main.py <pokemon_name>")
        sys.exit(1)
    
    return sys.argv[1]

def construct_paste_content(pokemon_data):
    """
    Constructs the title and body text for PasteBin.

    Parameters:
        pokemon_data (dict): Pokémon information.

    Returns:
        tuple: (title, body) where title is formatted and body is a list of abilities.
    """
    name = pokemon_data["name"].capitalize()
    abilities = [f"- {ability['ability']['name']}" for ability in pokemon_data["abilities"]]

    title = f"{name}’s Abilities"
    body = "\n".join(abilities)

    return title, body

def main():
    """
    Main function to fetch Pokémon info and create a PasteBin paste.
    """
    pokemon_name = get_pokemon_name()
    pokemon_data = get_pokemon_info(pokemon_name)

    if pokemon_data:
        title, body = construct_paste_content(pokemon_data)
        paste_url = create_paste(title, body, expire_date="1M", private=True)
        print(f"Paste created: {paste_url}")
    else:
        print("Failed to retrieve Pokémon information.")

if __name__ == "__main__":
    main()

