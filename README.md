# Simple HTTP Login-Form BruteForce
### Brute-forcing simple HTTP-login-form with Python3 by 0xhawwk 

**A python script to replace BurpSuite :)**

Modules required: which can be installed by using `pip` or `pip3`:
- time 
- sys 
- os 
- requests 

Run this script by `python3 PythSuite.py`

## Running this script 

1. You will be first prompted to enter the URL of the `HTTP-post-login-form`. You should copy the **URL** from the `Network Tab` from `Inspect Element`. For e.g. `http://10.10.10.10/login`
2. Then it should prompt if you want to choose a username wordlist. Type `y` if you want to add an wordlist. Then add the location of the wordlist. For e.g. `/usr/share/wordlists/username.txt`. If you want to enter a single username. type `n` and then type the username in the next question.
3. Then it should prompt if you want to choose a password wordlist. Type `y` if you want to add an wordlist. Then add the location of the wordlist. For e.g. `/usr/share/wordlists/rockyou.txt`. If you want to enter a single password. type `n` and then type the password in the next question.
4. Then add the first input field of the Login form. For e.g. Commonly for login form `username` is used 
5. Then add the second input field of the login form. For e.g. Commonly for login form in second field `password` is used 
6. You can get all these input fields from the `Network Tab` in `Inspect Element`. 
7. I hope you will like this tool replacing memory-hog BurpSuite lmfao for HTTP-login-forms 


**I will add more features, don't worry :)**
~ <3 from 0xhawwk
