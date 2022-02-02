#!/usr/bin/python3
"""Import module"""


import json

"""Define a function"""
"""to_json_string, parametres - my_obj"""


def to_json_string(my_obj):
    """Return the JSON representation of an object"""
    return(json.dumps(my_obj))
