#!/usr/bin/python3
"""
This script that fetches https://intranet.hbtn.io/status
"""

from urllib.request import urlopen
with urlopen('https://intranet.hbtn.io/status') as response:
    res = response.read()
print('Body response:')
print('\t' + '- type: ' + format(type(res)))
print('\t' + '- content: ' + str(res))
print('\t' + '- utf8 content: ' + res.decode('utf-8'))
