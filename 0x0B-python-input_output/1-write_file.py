#!/usr/bin/python3
"""function"""


def write_file(filename="", text=""):
    """function"""
    with open(filename, "w") as file:
        return file.write(text)
        file.close()
