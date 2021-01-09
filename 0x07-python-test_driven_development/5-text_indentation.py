#!/usr/bin/python3
"""prints new lines and indents"""


def text_indentation(text):
    """prints new line and indents"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text2 = text.replace(". ", ".").replace("? ", "?").replace(": ", ":")
    text3 = text2.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n")
    print(t2, end="")
