#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename) as file:
        file.write(text)
        file.close()
