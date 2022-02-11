#!/usr/bin/python3
"""Define a class"""
from models.base import Base


class Rectangle(Base):
    """The class name is Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Function constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Method setter and property in width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Method setter and property in height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
