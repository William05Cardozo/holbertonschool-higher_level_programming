#!/usr/bin/python3
"""Import a module"""


import json

"""Define a function"""
"""save_to_json_file, parametres - my_obj, filename"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        return(json.dump(my_obj, f))
