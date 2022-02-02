#!/usr/bin/python3
"""Import a module"""


import json

"""Define a function"""
"""from_json_string, parametres - my_str"""


def from_json_string(my_str):
    """Return an object presented by a Json string"""
    return(json.loads(my_str))
