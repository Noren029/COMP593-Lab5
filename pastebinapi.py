import requests
from credentials import PASTEBIN_API_KEY

PASTEBIN_URL = "https://pastebin.com/api/api_post.php"

def create_paste(title, content, expire_date="1M", private=True):
    """
    Uploads content to Pastebin.

    Parameters:
        title (str): Paste title.
        content (str): Paste content.
        expire_date (str): Expiration time (e.g., "1M" for 1 month).
        private (bool): Whether the paste is private.

    Returns:
        str: URL of the created paste or error message.
    """
    paste_data = {
        "api_dev_key": PASTEBIN_API_KEY,
        "api_paste_code": content,
        "api_paste_name": title,
        "api_paste_private": "1" if private else "0",
        "api_paste_expire_date": expire_date,
        "api_option": "paste"
    }

    response = requests.post(PASTEBIN_URL, data=paste_data)

    return response.text if response.status_code == 200 else f"Error: {response.text}"
