import json
import requests
#--------------------------------------
def getdomains():
    domains_json_tm = requests.get("https://api.mail.tm/domains", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }).text
    domains_json_gw = requests.get("https://api.mail.gw/domains", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }).text  
    domain_tm = json.loads(domains_json_tm)["hydra:member"][0]["domain"]
    domain_gw = json.loads(domains_json_gw)["hydra:member"][0]["domain"]
    return {
        "DOMAIN": [
            {
                "service": "tm",
                "domain":  domain_tm
            },
            {
                "service": "gw",
                "domain" : domain_gw
            }
        ]
    }
#---------------------------------------------------------------