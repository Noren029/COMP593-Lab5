import requests

def fetch_pokemon_data(pokemon_name):
    """Fetch data from the PokeAPI for a given Pokémon name."""
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Returns the JSON data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def construct_content(pokemon_data):
    """Constructs a formatted string with Pokémon information."""
    name = pokemon_data["name"].capitalize()
    abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
    abilities_str = ", ".join(abilities)
    return f"{name} has the following abilities: {abilities_str}."
