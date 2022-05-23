#!/usr/bin/python3
"""
This script send a request to the URL and
manage a HTTPError
"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
