import json , requests

def GetMsg(token , service):
    R = requests.get(f"https://api.mail.{service}/messages" , headers = {
        "authorization": f"Bearer {token}" ,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    })
    if json.loads(R.text)["hydra:member"] == []:
        return "None Email Found"
    else:
     id = json.loads(R.text)["hydra:member"][0]["id"]
     return id