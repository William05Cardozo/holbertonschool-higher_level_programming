#!/usr/bin/python3
"""Define a class"""


class MyList(list):
    """The class is a List"""
    """Print a list in ascending order"""
    def print_sorted(self):
        print(sorted(self))
