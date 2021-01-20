#!/usr/bin/python3
"""function"""


def append_write(filename="", text=""):
    """function"""
    with open(filename, "a") as file:
        return file.write(text)
        file.close()
