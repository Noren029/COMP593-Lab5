import sys
import pokeapi1  # Import functions from pokeapi.py
import pastebinapi1  # Import the function from pastebin_api.py

def get_pokemon_name():
    """Gets the Pokémon name from the command line argument."""
    if len(sys.argv) < 2:
        print("Error: Please provide a Pokémon name.")
        sys.exit(1)
    return sys.argv[1].lower()

def main():
    """Main function that runs the script."""
    pokemon_name = get_pokemon_name()  # Get Pokémon name from command-line
    pokemon_data = pokeapi1.fetch_pokemon_data(pokemon_name)  # Fetch Pokémon data
    
    if pokemon_data:
        content = pokeapi1.construct_content(pokemon_data)  # Construct formatted content
        print("Posting data to Pastebin...")
        
        # Post to Pastebin
        paste_url = pastebinapi1.pastebin_post(f"{pokemon_name.capitalize()} Abilities", content)
        
        if paste_url:
            print(f"Paste successfully created! You can view it here: {paste_url}")
        else:
            print("Failed to create paste.")
    else:
        print(f"Failed to fetch data for {pokemon_name}.")

if __name__ == "__main__":
    main()
