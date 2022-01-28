#!/usr/bin/python3
"""Define a class"""


class Rectangle:
    """The class is a Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
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
            self.__height = vale

    def area(self):
        return(self.__width * self.__height)
    """Print the area of Rectangle"""

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return(0)
        return(self.width + self.__height) * 2
    """Print the perimeter of Rectangle"""

    def __str__(self):
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))
        return(string)

    def __repr__(self):
        return("Rectangle({}, {})".format(self.__width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
