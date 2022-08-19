import requests
#---------------------------------------------------
from Seprator import discordorother
#----------------------------------------------------
def getfullmsg(id , token , service):
    R = requests.get(f"https://api.mail.{service}/messages/{id}" , headers = {
        "authorization": f"Bearer {token}" ,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    })
    discordorother(R.text)

