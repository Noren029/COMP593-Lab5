'''pastebin_api.py - Post a dad joke to pastebin.com, return URL
COMP 593 Scripting Applications Winter 2025 Lab 5
Louis Bertrand <louis.bertrand@flemingcollege.ca>

Usage:
Import as a module.

'''

import requests
import credentials  # Import the API key from credentials.py

POST_URL = 'https://pastebin.com/api/api_post.php'

def pastebin_post(title, body_text):
    """Creates a new PasteBin paste with Pokémon details."""
    post_params = {
        'api_dev_key': credentials.API_DEV_KEY,  # Securely fetch API key
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_private': '1',  # 1 = unlisted
        'api_paste_name': title,
        'api_paste_expire_date': '1M'  # 1 Month expiry
    }

    response = requests.post(POST_URL, data=post_params)
    
    if response.ok:
        return response.text  # Return the PasteBin URL
    else:
        print(f"Error creating PasteBin paste: {response.text}")
        return None  # Indicate failure

if __name__ == "__main__":
    print("Please import this module.")
