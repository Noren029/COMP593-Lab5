'''log_matching.py - Module to help analyze a log file using regular expressions.
COMP 593 Scripting Applications - Winter 2025 (Week 5)
Louis Bertrand <louis.bertrand@flemingcollege.ca>

Usage: Import this module into your main program

### STUDENTS: PLEASE ADD THE STANDARD ACADEMIC INTEGRITY STATEMENT.###
# This program is strictly my own work. Any material beyond course learning
# materials that is taken from the Web or other sources is properly cited,
# giving credit to the original author(s).

'''
import requests

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
