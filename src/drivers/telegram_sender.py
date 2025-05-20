import requests
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
chat_id = os.getenv("CHAT_ID")


def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    requests.post(url, data=payload)
    