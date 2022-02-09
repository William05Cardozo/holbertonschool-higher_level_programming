#!/usr/bin/python3
"""Define a class"""


class Base:
    """The class name is Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init the function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects 
