#!/usr/bin/python3

def uppercase(str):
    nstring = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            nstring += chr(ord(str[i]) - 32)
            continue
        nstring += str[i]
        print("{}".format(nstring))
