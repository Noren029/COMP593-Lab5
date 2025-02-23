import requests
import sys
from credentials import PASTEBIN_API_KEY

def create_paste(title, body):
    pastebin_url = "https://pastebin.com/api/api_post.php"
    data = {
        "api_dev_key": PASTEBIN_API_KEY,
        "api_option": "paste",
        "api_paste_code": body,
        "api_paste_name": title,
        "api_paste_expire_date": "1M"
    }
    response = requests.post(pastebin_url, data=data)
    if response.status_code == 200:
        return response.text
    else:
        print("Error: Failed to create Pastebin paste.")
        sys.exit(1)
