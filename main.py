import sys 
import pokeapi  # Import the functions from pokeapi.py
import pastebinapi  # Import the functions from pastebinapi.py

def get_pokemon_name():
    """Gets the Pokémon name from the command line argument."""
    if len(sys.argv) < 2:
        print("Error: Please provide a Pokémon name.")
        sys.exit(1)
    return sys.argv[1].lower()

def main():
    """Main function to fetch Pokémon data and post to Pastebin."""
    pokemon_name = get_pokemon_name()  # Get Pokémon name from command-line
    pokemon_data = pokeapi.fetch_pokemon_data(pokemon_name)  # Fetch Pokémon data
    
    if pokemon_data:
        content = pokeapi.construct_content(pokemon_data)  # Construct formatted content
        if content:
            print("Posting data to Pastebin...")
            paste_url = pastebinapi.pastebin_post(f"{pokemon_name.capitalize()} Abilities", content)
            
            if paste_url:
                print(f"Paste successfully created! You can view it here: {paste_url}")
            else:
                print("Failed to create paste.")
        else:
            print("Content is empty. Failed to construct content.")
    else:
        print(f"Failed to fetch data for {pokemon_name}.")

if __name__ == "__main__":
    main()
