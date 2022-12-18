import requests

def GetTokenInfo(email , passw , service):
    R = requests.post(f"https://api.mail.{service}/token", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }, json={
        "address": email.lower(),
        "password": passw
    })
    return R.text
