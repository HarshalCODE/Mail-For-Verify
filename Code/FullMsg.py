import requests , json
from colorama import Fore , Style

def FullMsg(id , token , service):
    R = requests.get(f"https://api.mail.{service}/messages/{id}" , headers = {
        "authorization": f"Bearer {token}" ,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    })
    Full_Msg = json.loads(fixjson(R.text))
    print(f"{Fore.LIGHTWHITE_EX}From : " + Full_Msg["from"]["address"] + f"{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}Subject : " + Full_Msg["subject"] + f"{Style.RESET_ALL}")
    print(f"{Fore.LIGHTWHITE_EX}Text : " + (Full_Msg["text"]).replace("  ", "") + f"{Style.RESET_ALL}")


def fixjson(badjson):
    s = badjson
    idx = 0
    while True:
        try:
            start = s.index( '": "', idx) + 4
            end1  = s.index( '",\n',idx)
            end2  = s.index( '"\n', idx)
            if end1 < end2:
                end = end1
            else:
                end = end2
            content = s[start:end]
            content = content.replace('"', '\\"')
            s = s[:start] + content + s[end:]
            idx = start + len(content) + 6
        except:
            return s