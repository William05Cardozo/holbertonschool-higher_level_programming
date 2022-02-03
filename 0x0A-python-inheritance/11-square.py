#!/usr/bin/python3
"""Import module"""


Rectangle = __import__('9-rectangle').Rectangle

"""Define a class"""


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return Square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
