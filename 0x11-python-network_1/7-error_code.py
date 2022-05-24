#!/usr/bin/python3
"""
This script send a request to the URL and
manage a HTTPError
"""

from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print('Error code:', r.status_code)
