import re
import os
import webbrowser
#--------------------------------------------------------
def remove(string):
    return string.replace("  ", "")
#---------------------------------------------------------
def discordorother(data):
    if data["subject"] == "Verify Email Address for Discord":
        link = len(data["text"].split(" "))
        print("Discord Verify Link : " +data["text"].split(" ")[link - 1])
        webbrowser.open(data["text"].split(" ")[link - 1])
    else:
     print("From : " + data["from"]["address"])
     print("From Name :" + data["from"]["name"])
     print("Subject : " + data["subject"])
     print("Text : " + remove(data["text"]))
