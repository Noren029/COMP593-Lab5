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
from pokeapi import fetch_abilities
from pastebinapi import create_pastebin_paste

def main():
    if len(sys.argv) != 5:
        print("Usage: python main.py <api_dev_key> <user_api_key> <paste_title> <paste_content>")
        sys.exit(1)
    
    api_dev_key = sys.argv[1]
    user_api_key = sys.argv[2]
    paste_title = sys.argv[3]
    
    abilities = fetch_abilities()
    if abilities:
        abilities_content = "\n".join(abilities)
        paste_url = create_pastebin_paste(api_dev_key, user_api_key, paste_title, abilities_content)
        print(f"Paste created: {paste_url}")
    else:
        print("Failed to fetch abilities.")

if __name__ == "__main__":
    main()
