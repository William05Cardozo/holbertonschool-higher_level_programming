#!/usr/bin/python3
"""
This script send a request to the url and
displays the value of the X-Request-Id
"""

from urllib.request import urlopen
from sys import argv

with urlopen(argv[1]) as response:
    res = response.getheader('X-Request-Id')
    print(res)
