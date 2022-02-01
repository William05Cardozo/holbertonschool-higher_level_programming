#!/usr/bin/python3
"""Declaration of function"""


def inherits_from(obj, a_class):
    """Function inherits_from"""
    """Return True if the object is an instance
    if not return False"""
    return(type(obj) != a_class and isinstance(obj, a_class))
