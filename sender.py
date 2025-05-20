import requests
from dotenv import load_dotenv
import os

load_dotenv()

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)
    
token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")
message = "Hello World"

send_telegram_message(token, chat_id, message)
