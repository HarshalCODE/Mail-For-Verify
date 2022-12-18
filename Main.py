from time import sleep
import threading , os , sys , json
from colorama import Fore, Style

try:
    sys.dont_write_bytecode = True
    os.system("cls")
    from Code.Domains import Domains
    from Code.FullMsg import FullMsg
    from Code.GetMsg import GetMsg
    from Code.GetToken import GetTokenInfo
    from Code.Mail import CreateMail
except:
    os.system("clear")


class MailGen:
    def __init__(self) -> None:
        self.mailgen_layout = f"""{Fore.LIGHTMAGENTA_EX}
        ███████╗███╗░░░███╗░█████╗░██╗██╗░░░░░  ░██████╗░███████╗███╗░░██╗
        ██╔════╝████╗░████║██╔══██╗██║██║░░░░░  ██╔════╝░██╔════╝████╗░██║
        █████╗░░██╔████╔██║███████║██║██║░░░░░  ██║░░██╗░█████╗░░██╔██╗██║
        ██╔══╝░░██║╚██╔╝██║██╔══██║██║██║░░░░░  ██║░░╚██╗██╔══╝░░██║╚████║
        ███████╗██║░╚═╝░██║██║░░██║██║███████╗  ╚██████╔╝███████╗██║░╚███║
        ╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝\n\n{Style.RESET_ALL}"""
        print(self.mailgen_layout)
        print(f'{Fore.BLACK}-------------------------------------------------------------------------{Style.RESET_ALL}')

        threading.Thread(target=lambda: MailGen.sm_print(
            f"{Fore.LIGHTRED_EX}Loading Email Domains...\n\n{Style.RESET_ALL}")).start()
        self.domain_present = Domains()
        self.option_dir = []
        for i in range(len(self.domain_present)):
            dom = self.domain_present[i]["EMAIL_DOMAIN"]
            print(f"{Fore.CYAN}{i+1}. {Fore.LIGHTGREEN_EX}{dom}{Style.RESET_ALL}")

            self.option_dir.append({
                "COUNT_NO": i+1,
                "SITE": self.domain_present[i]["SITE_NAME"],
                "DOMAIN": self.domain_present[i]["EMAIL_DOMAIN"]
            })

        print(f'{Fore.BLACK}-------------------------------------------------------------------------{Style.RESET_ALL}')
        Opt = int(input("Choose A Domain Option : "))
        for dicts in self.option_dir:
            if dicts["COUNT_NO"] == Opt:
                self.domain = dicts["DOMAIN"]
                self.site = dicts["SITE"]

        try:
            self.site
            
        except:
            os.system("cls")
            print(self.mailgen_layout)
            print(
                f"{Fore.LIGHTRED_EX}[ERROR] Invalid Option Choosen ! Exiting...{Style.RESET_ALL}")
            sleep(2)
            exit(0)
        
        MailGen.TempMail(self)

    def sm_print(text):
        if text == "part":
            print(f'{Fore.BLACK}-------------------------------------------------------------------------{Style.RESET_ALL}')
            return True
        else:
         for letter in text:
            print(letter, end='', flush=True)
            sleep(0.025)

    def TempMail(self):
        os.system("cls")
        print(self.mailgen_layout )
        if self.site == "MAIL.TM":
               self.service = "tm"
        elif self.site == "MAIL.GW":
               self.service = "gw"

        MailInfo = CreateMail(self.domain, self.service)
        self.mail = MailInfo["Credentials"][0]["Mail"]
        self.passw = MailInfo["Credentials"][0]["Pass"]

        self.token = (json.loads(GetTokenInfo(self.mail , self.passw , self.service)))["token"]
        MailGen.sm_print("part")
        print(f'{Fore.LIGHTBLUE_EX}Email :  {Fore.CYAN}{self.mail}{Style.RESET_ALL}')
        print(f'{Fore.LIGHTBLUE_EX}Passw :  {Fore.CYAN}{self.passw}{Style.RESET_ALL}')

        x = True
        while x:
            MailGen.sm_print("part")
            answer = input(f"{Fore.GREEN}Want To Fetch Email ? Y/N : {Style.RESET_ALL}")
            if answer.lower() == "y":
                id = GetMsg(self.token, self.service)
                if id == "None Email Found":
                    print(f"{Fore.RED}[!] None Email Found {Style.RESET_ALL}")
                else:
                   FullMsg(id , self.token , self.service)
            else:
                exit(0)


if __name__ == "__main__":
    Email = MailGen()
