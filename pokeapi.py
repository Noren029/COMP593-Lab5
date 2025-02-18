import requests
import sys

def fetch_abilities():
    url = "https://pokeapi.co/api/v2/ability/"
    abilities = []
    
    # Paginate through abilities if necessary
    while url:
        response = requests.get(url)
        data = response.json()
        abilities.extend([ability['name'] for ability in data['results']])
        url = data['next']
    
    return abilities

if __name__ == "__main__":
    abilities = fetch_abilities()
    if abilities:
        print(f"Fetched {len(abilities)} abilities.")
    else:
        print("No abilities found.")
