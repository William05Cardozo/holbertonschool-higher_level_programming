#!/usr/bin/python3
"""
This script send a request to the URL and
manage a HTTPError
"""

from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as error:
        print("Error code: {}".format(error.status_code))
