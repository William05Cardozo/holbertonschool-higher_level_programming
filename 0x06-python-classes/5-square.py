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
        and return no line"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the square area"""
        return(self.__size) ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        for iter in range(self.__size):
            print("#" * self.__size)
            """Print the Square, in case Size is 0 print an empty line"""
            """Return none"""
