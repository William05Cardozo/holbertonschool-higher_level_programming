#!/usr/bin/python3
"""
This script take my GitHub credentials and uses the GITHUB API
display my id
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    rq = requests.get(url, auth=(username, password))

    if rq.status_code == 200:
        js = rq.json()
        print(js.get('id'))
    else:
        print('None')
