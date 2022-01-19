#!/usr/bin/python3
"""Define a class"""


class Square:
    """The class is a Square"""

    def __init__(self, size=0):
        """Init the class"""

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


        """Define a class"""

    def area(self):
        """This class is a area"""
        """Return the square area"""
        return(self.__size) ** 2
