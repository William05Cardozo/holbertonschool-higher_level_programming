#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    ndict = {}
    for i in a_dictionary:
        ndict.update({i: (a_dictionary[i] * 2)})
    return(ndict)
