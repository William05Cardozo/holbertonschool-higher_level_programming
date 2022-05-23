#!/usr/bin/python3
"""
This script send a POST Request to the passed URL,
with the email
"""

from sys import argv
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    r = urllib.request.Request(url, data)
    with urllib.request.urlopen(r) as response:
        print(response.read().decode('utf-8'))
