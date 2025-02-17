




import requests
import sys

def get_pokemon_name():
    """Gets the Pokémon name from the command line parameter."""
    if len(sys.argv) < 2:
        print("Error: Please provide a Pokémon name.")
        sys.exit(1)
    return sys.argv[1].lower()

def fetch_pokemon(pokemon_name):
    """Fetches Pokémon data from the PokéAPI."""
    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"  # Corrected URL
    resp = requests.get(URL)
    if resp.ok:
        return resp.json()
    else:
        print(f"Error: Pokémon '{pokemon_name}' not found.")
        sys.exit(1)

def construct_content(pokemon_data):
    """Constructs a formatted string with Pokémon information."""
    name = pokemon_data["name"].capitalize()
    height = pokemon_data["height"]
    weight = pokemon_data["weight"]
    abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
    
    abilities_str = ", ".join(abilities)
    return f"{name} is a Pokémon with height {height} and weight {weight}. It has abilities: {abilities_str}."

if __name__ == "__main__":
    print("Please import this module.")
