'''dadjokes.py - Request a dad joke and paste to pastebin.
COMP 593 Scripting Applications Winter 2025 Lab 5
Louis Bertrand <louis.bertrand@flemingcollege.ca>

Usage:
python dadjokes.py <subject>
where subject is a keyword to search in the dad jokes database.

'''


from sys import argv
import poke_api
import pastebin_api

def get_subject():
    
    if len(argv) > 1:
        return str(argv[1]).strip().lower()
    else:
        print("Expecting to provide charizard information...")
        exit()

def main():
    charizard = get_subject()
    charizard_data = poke_api.fetch_pokemon(charizard)
    # Reformat data from pokeAPI site
    paste_url = pastebin_api.pastebin_post(charizard_data)
    print(paste_url)

if __name__ == "__main__":
    main()