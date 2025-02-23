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
from pokeapi import get_pokemon_abilities
from pastebinapi import create_paste

def format_paste_title(pokemon_name):
    return f"Abilities of {pokemon_name.title()}"

def format_paste_body(pokemon_name, abilities):
    return f"{pokemon_name.title()} has the following abilities:\n" + "\n".join(abilities)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <pokemon_name>")
        sys.exit(1)
    
    pokemon_name = sys.argv[1]
    abilities = get_pokemon_abilities(pokemon_name)
    title = format_paste_title(pokemon_name)
    body = format_paste_body(pokemon_name, abilities)
    paste_url = create_paste(title, body)
    print("Paste created:", paste_url)


