

import urllib.requests

addr = 'https://api.myip.org'
response = urrlib.request.urlopen(addr)
html = response.read()
print(html)

