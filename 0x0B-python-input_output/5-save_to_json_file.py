#!/usr/bin/python3
"""Import a module"""


import json

"""Define a function"""
"""save_to_json_file, parametres - my_obj, filename"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representatio"""
    with open(filename, 'w', encoding='utf-8') as f:
        return(json.dump(my_obj, f))
