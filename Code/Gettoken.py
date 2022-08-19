import requests
#---------------------------------------------------------------
def getinfo(email , passw , service):
    print(f'\033[96mEmail :   {email.lower()}\033[00m')
    print(f'\033[96mPassw :   {passw}\033[00m')
    print("---------------------------------------------------------------")
    R = requests.post(f"https://api.mail.{service}/token", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    }, json={
        "address": email.lower(),
        "password": passw
    })
    return R.text
#---------------------------------------------------------------