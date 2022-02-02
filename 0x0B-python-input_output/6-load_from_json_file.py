#!/usr/bin/python3
"""Import a module"""


import json
"""Define a function"""
"""load_from_file, parametres - filename"""


def load_from_json_file(filename):
    """Function that creates an object"""
    with open(filename, 'r', encoding='utf-8') as f:
        return(json.load(f))
