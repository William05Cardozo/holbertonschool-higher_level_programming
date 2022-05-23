#!/usr/bin/python3
"""
This script that fetches https://intranet.hbtn.io/status
Module: requests
"""

import requests
r = requests.get('https://intranet.hbtn.io/status')
print('Body response:')
print('\t' + '- type: ' + format(type(r)))
print('\t' + '- content: ' + str(r.text))
