#!/usr/bin/python3
"""Define a class"""


class Student:
    """The class name is Student"""


    def __init__(self, first_name, last_name, age):
        """Init the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Method Json"""
        return(self.__dict__)
