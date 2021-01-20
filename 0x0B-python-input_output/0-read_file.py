#!/usr/bin/python3
"""function"""


def read_file(filename=""):
    """function"""
    with open(filename) as reader:
        print(reader.read())
        reader.close()
