import requests
import credentials  # Ensure you have credentials.py with your API key

POST_URL = 'https://pastebin.com/api/api_post.php'

def pastebin_post(title, body_text):
    """Creates a new Pastebin paste with Pokémon details."""
    post_params = {
        'api_dev_key': credentials.API_DEV_KEY,  # Fetch API key from credentials.py
        'api_option': 'paste',
        'api_paste_data': body_text,  # Correct parameter
        'api_paste_private': '1',  # 1 = unlisted
        'api_paste_name': title,
        'api_paste_expire_date': '1M'  # 1 Month expiry
    }

    response = requests.post(POST_URL, data=post_params)
    
    if response.ok:
        return response.text  # Return the Pastebin URL
    else:
        print(f"Error creating Pastebin paste: {response.text}")
        return None  # Indicate failure
