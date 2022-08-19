import string
import random
import requests
#---------------------------------------------------------------
def randomamil(domain, service):
    to_create = "".join([random.choice(string.ascii_letters)for i in range(10)]) + '@' + domain
    mail_pass = "".join([random.choice(string.digits) for i in range(5)])
    R = requests.post(f"https://api.mail.{service}/accounts", headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }, json={
        "address": to_create,
        "password": mail_pass
    })
    return {
            "Return_Data": R.text,
            "Credentials": [
                {
                    "Mail": to_create,
                    "Pass": mail_pass
                }
            ],
            "service" : service
        }
#---------------------------------------------------------------