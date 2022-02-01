#!/usr/bin/python3
"""Define a class"""


class BaseGeometry:
    """The class name is BaseGeometry"""
    """Define a Function"""

    def area(self):
        raise Exception("area() is not implemented")
    """Print a error message"""

    def integer_validator(self, name, value):
        """Function integer_validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
