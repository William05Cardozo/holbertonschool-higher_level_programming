#!/usr/bin/python3
"""Import"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""Define a class"""


class Rectangle(BaseGeometry):
    """The class is a Rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    """Method area"""
    def area(self):
        return(self.__width * self.__height)

    """Method str"""
    def __str__(self):
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
