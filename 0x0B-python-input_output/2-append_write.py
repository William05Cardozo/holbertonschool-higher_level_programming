#!/usr/bin/python3
"""Function append_write"""
"""Parametres - filename, text"""


def append_write(filename="", text=""):
    """Add a string"""
    with open(filename, 'a', encoding='utf-8') as append:
        return(append.write(text))
