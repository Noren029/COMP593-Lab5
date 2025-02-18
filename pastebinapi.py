# pastebin_api.py
import requests
import credentials

PASTEBIN_API_URL = "https://pastebin.com/api/api_post.php"
PASTEBIN_API_KEY = credentials.PASTEBIN_API_KEY  # Replace with your API key in credentials.py

def create_pastebin_paste(title, content):
    data = {
        "api_dev_key": PASTEBIN_API_KEY,
        "api_option": "paste",
        "api_paste_name": title,
        "api_paste_code": content,
        "api_paste_private": "1",  # 1 = unlisted, 2 = private
        "api_paste_expire_date": "10M",  # Expires in 10 minutes
    }
    response = requests.post(PASTEBIN_API_URL, data=data)
    
    if response.status_code == 200:
        return response.text  # Returns the paste URL
    else:
        return "Error: Unable to create PasteBin paste"