import json , requests


def Domains():
    domains_json_tm = requests.get("https://api.mail.tm/domains", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }).text
    domains_json_gw = requests.get("https://api.mail.gw/domains", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }).text  
    return [
            {
                "SITE_NAME": "MAIL.TM",
                "EMAIL_DOMAIN":  json.loads(domains_json_tm)["hydra:member"][0]["domain"]
            },
            {
                "SITE_NAME": "MAIL.GW",
                "EMAIL_DOMAIN" : json.loads(domains_json_gw)["hydra:member"][0]["domain"]
            }
        ]