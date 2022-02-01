#!/usr/bin/python3
"""Function write_file"""
"""Parametres - filename, text"""


def write_file(filename="", text=""):
    """write in the file"""
    with open(filename, 'w', encoding='utf-8') as file:
        print(file.write(text))
