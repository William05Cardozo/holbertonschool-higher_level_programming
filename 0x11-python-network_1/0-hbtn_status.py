#!/usr/bin/python3
"""
This script that fetches https://intranet.hbtn.io/status
"""

import urllib.request
response = urllib.request.urlopen('https://intranet.hbtn.io/status')
res = response.read()
print('Body response:')
print('\t - type: ' + format(type(res)))
print('\t - content: ' + str(res))
print('\t - utf8 content: ' + res.decode('utf-8'))
