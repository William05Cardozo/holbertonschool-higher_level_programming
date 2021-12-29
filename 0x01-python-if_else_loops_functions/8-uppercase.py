#!/usr/bin/python3
def uppercase(str):
    nstring = ""
    
    for a in range(len(str)):
        if ord(str[a]) >= 97 and ord(str[a]) <= 122:
            nstring += chr(ord(str[a]) - 32)
            continue
        nstring += str[a]
        print("{}".format(nstring))
