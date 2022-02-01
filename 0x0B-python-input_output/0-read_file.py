#!/usr/bin/python3
"""Function read_file"""
"""Parametres - filename"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as file:
        print(file.read())
