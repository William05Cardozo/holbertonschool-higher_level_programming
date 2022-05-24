#!/usr/bin/python3
"""
This script takes in a letter and send a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
The letter must be a sent in the variable: q
"""

from sys import argv
import requests

if __name__ == "__main__":
    arg = ""
    if len(argv) == 2:
        arg = argv[1]
    try:
        url = "http://0.0.0.0:5000/search_user"
        value = {"q": arg}
        rq = requests.post(url, data=value)
        js = rq.json()
        if js:
            print('[{}] {}'.format(js.get('id'), js.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
