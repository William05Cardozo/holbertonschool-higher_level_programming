#!/usr/bin/python3
"""Import module"""


Rectangle = __import__('9-rectangle').Rectangle

"""Define a class"""

class Square(Rectangle):
    """The name class is Square"""

    def __init__(self, size):
        """method init"""
        self.integer_validator("size", size)
        super().__init__(size, size)
