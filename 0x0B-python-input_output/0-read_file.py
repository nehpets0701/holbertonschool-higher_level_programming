#!/usr/bin/python3
"""function"""


def read_file(filename=""):
    """function"""
    with open(filename) as reader:
        for x in reader:
            print (x, end="")
        reader.close()
