import sys
from pokeapi import get_pokemon_abilities
from pastebinapi import create_pastebin_paste

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <pokemon_name>")
        return
    
    pokemon_name = sys.argv[1]
    abilities = get_pokemon_abilities(pokemon_name)
    
    if isinstance(abilities, str):
        print(abilities)
        return
    
    content = f"Abilities of {pokemon_name.capitalize()}:\n" + "\n".join(abilities)
    paste_url = create_pastebin_paste(f"{pokemon_name.capitalize()} Abilities", content)
    print(f"Paste created: {paste_url}")

if __name__ == "__main__":
    main()