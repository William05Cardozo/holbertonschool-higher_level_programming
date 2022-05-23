#!/usr/bin/python3
"""
This script send a POST Request to the passed URL,
with the email
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    value = argv[2]
    r = requests.post(url, data={'email': value})
    print(r.text)
