#!/usr/bin/python3
"""Difine a class"""


class Rectangle:
    """The class is a Rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        """Init the class"""
        """With the attributes width and height"""

        """We aply the method Property and Setter"""
    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        total = ""
        if self.__height == 0 or self.width == 0:
            return(total)
        for i in range(self.__height):
            total += ("#" * self.__width)
            if i is not self.__height - 1:
                total += "\n"
        return(total)

    def area(self):
        return(self.__width * self.__height)
    """Print the area of Rectangle"""

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        return(self.width + self.__height) * 2
    """Print the perimeter of Rectangle"""
