import os
#-----------------------------------------------------
from Code.Domains import getdomains
from Runner import tempgenemail
from Runner import loginold
#----------------------------------------------------
def loginmailgen():
    os.system("cls")
    print("""\033[94m
███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ░██████╗░███████╗███╗░░██╗
██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔════╝░██╔════╝████╗░██║
█████╗░░██╔████╔██║███████║██║██║░░░░░  ██║░░██╗░█████╗░░██╔██╗██║
██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ██║░░╚██╗██╔══╝░░██║╚████║
███████╗██║░╚═╝░██║██║░░██║██║███████╗  ╚██████╔╝███████╗██║░╚███║
╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝ \n\n\033[00m""")
    print("\033[95mLoading Email Gen.. \n ------------------------------------------------------------------\033[00m")
#---------------------------------------------------------------------------------
def loginoldmail():
    Email = input("Enter Email Adress From Config : ")
    Password = input("Enter Passowrd of Email Adress : ")
    Service = input("Service name tm\gw : ")
    loginold(Email.lower() , Password.lower() , Service.lower())

#-----------------------------------------------------------------------------------
def createrandommail():
    domain_json = getdomains()
    domain_1 = domain_json["DOMAIN"][0]["domain"]
    domain_2 = domain_json["DOMAIN"][1]["domain"]

    print(f"\033[93m 1. {domain_1} [Avaliable Permanent] \n 2. {domain_2} [Only Valid For 10 Min]\033[00m")
    print("\033[95m------------------------------------------------------------------ \033[00m")
    domain = input("Choose A Emaill Domain Adress : ")
    if domain == "1":
        tempgenemail(domain_json , 0)
    if domain == "2":
        tempgenemail(domain_json , 1)

    


if __name__ == "__main__":
        loginmailgen()
        print(f"\033[93m 1. Email Gen \n 2. Login To Old Mail\033[00m")
        print("-----------------------------------------------------------------------")
        answer = input("Which U Whould Like To Choose :")
        os.system("cls")
        if answer == "1":
            createrandommail()
        if answer == "2":
            loginoldmail()

