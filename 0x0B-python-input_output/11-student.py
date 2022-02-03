#!/usr/bin/python3
"""Define a class"""


class Student:
    """The class name is Student"""

    def __init__(self, first_name, last_name, age):
        """Init the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method Json"""
        if type(attrs) is list and all([type(i) == str for i in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return(self.__dict__.copy())

    def reload_from_json(self, json):
        """Function loads attributes from Json"""
        for key, value in json.items():
            self.__dict__[key] = value
