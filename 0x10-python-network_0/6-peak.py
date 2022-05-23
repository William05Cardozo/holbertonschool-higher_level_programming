#!/usr/bin/python3
"""
Technical Interview:
Write a function that finds a peak in a list of unsorted integers.
6-peak.py(this archived) must contain the funtion
6-peak.txt must contain the complexity of your algorithm
"""


def find_peak(list_of_integers):
    """This function find a peak"""

    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]
