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
    
    if not pokemon_data:
        return None  # Return None if no data is found

    name = pokemon_data["name"].capitalize()
    height = pokemon_data["height"]
    weight = pokemon_data["weight"]

    # Extracting abilities correctly
    abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]

    abilities_str = ", ".join(abilities)
    
    content = f"{name} is a Pokémon with height {height} and weight {weight}. It has abilities: {abilities_str}."

    print("Constructed Content:", content)  # Debugging print
    
    return content


