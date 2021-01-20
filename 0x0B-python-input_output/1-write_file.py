#!/usr/bin/python3
"""function"""


def write_file(filename="", text=""):
    """function"""
    with open(filename) as file:
        file.write(text)
        file.close()
