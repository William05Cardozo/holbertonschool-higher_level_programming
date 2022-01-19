#!/usr/bin/python3
"""Define a class"""


class Square:
    """The class is a Square"""
    def __init__(self, size=0):
        self.size = size
        """Init the class"""

    @property
    def size(self):
        """Aply the method getter via property method and return Size"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Aply the method setter via property method
        Return no lines"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the square area"""
        return(self.__size) ** 2
