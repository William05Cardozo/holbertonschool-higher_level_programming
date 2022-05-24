#!/usr/bin/python3

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
