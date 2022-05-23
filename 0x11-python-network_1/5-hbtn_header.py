#!/usr/bin/python3
"""
This script send a request to the url and
displays the value of the X-Request-Id
"""

import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
