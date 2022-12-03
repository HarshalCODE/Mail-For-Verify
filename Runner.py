import os
import json
from colorama import Fore
from colorama import Style
#------------------------------------------------------
from Code.Randommail import randomamil
from Code.Gettoken import getinfo
from Code.getmessage import fetchmessage
from Code.getfullmsg import getfullmsg
#------------------------------------------------------
def tempgenemail(domain_json , co):
        os.system("cls")
        if co == 0:
         print(f"{Fore.GREEN} [!] Account Created {Style.RESET_ALL} \n")
        data = randomamil(
            domain_json["DOMAIN"][co]["domain"], domain_json["DOMAIN"][co]["service"])
        token_json = getinfo(data["Credentials"][0]["Mail"],
                             data["Credentials"][0]["Pass"], data["service"])
        print(f"{Fore.GREEN} [!] Token Fetched {Style.RESET_ALL}")
        x = True
        while x:
            answer = input("\033[94mWant To Fetch Email ? Y/N : \033[0m")
            if answer.lower() == "y":
                os.system("cls")
                id = fetchmessage(json.loads(token_json)["token"], data["service"])
                if id == "None Email Found":
                    print(f"{Fore.RED}[!]None Email Found {Style.RESET_ALL}")
                    break
                else:
                    getfullmsg(id , json.loads(token_json)["token"] , data["service"])
            else:
                exit(0)
#------------------------------------------------------
def loginold(email , passw , service):
        os.system("cls")
        token_json = getinfo(email,
                             passw, service)
        print(f"{Fore.GREEN} [!] Token Fetched {Style.RESET_ALL}")
        x = True
        while x:
            answer = input("\033[94mWant To Fetch Email ? Y/N : \033[0m")
            if answer.lower() == "y":
                os.system("cls")
                msg = fetchmessage(json.loads(token_json)["token"], service)
                if msg == "None Email Found":
                    print(f"{Fore.RED}[!]None Email Found {Style.RESET_ALL}")
                    break
                answer = input("\033[94mDo U Want To Fetch Full Msg Y/N :\033[0m")
                if answer.lower() == "y":
                    id =  input("\033[94mPlease Give Msg Id :\033[0m")
                    getfullmsg(id , json.loads(token_json)["token"] , service)
            else:
                exit(0)
