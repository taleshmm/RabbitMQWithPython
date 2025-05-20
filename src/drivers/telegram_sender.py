import requests

def send_telegram_message(message) -> None:
    token = "7637095888:AAE8wxobTNCG2YNgxzp49i1EoVlZkPeOhQ0"
    chat_id = "-1002550383518"
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    
    requests.post(url, data=payload)