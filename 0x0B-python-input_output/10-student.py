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
        if attrs is None:
            return(self.__dict__)
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except:
                pass
        """Return new list"""
        return(new_dict)
