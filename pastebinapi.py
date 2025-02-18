import requests
import sys

def create_pastebin_paste(api_key, user_api_key, title, content):
    url = "https://pastebin.com/api/api_post.php"
    data = {
        "api_dev_key": api_key,
        "api_user_key": user_api_key,
        "api_option": "paste",
        "api_paste_data": content,
        "api_paste_name": title,
        "api_paste_private": "0",  # Public paste
        "api_paste_expire_date": "N",  # No expiration
    }
    
    response = requests.post(url, data=data)
    return response.text

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python create_pastebin.py <api_dev_key> <user_api_key> <title> <content>")
        sys.exit(1)
    
    api_dev_key = sys.argv[1]
    user_api_key = sys.argv[2]
    title = sys.argv[3]
    content = sys.argv[4]
    
    paste_url = create_pastebin_paste(api_dev_key, user_api_key, title, content)
    print(f"Paste created: {paste_url}")
