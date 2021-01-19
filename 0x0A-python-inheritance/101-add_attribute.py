#!/usr/bin/python3
def add_attribute(obj, name, value):
    for i in dir(obj):
        if i == "__dict__":
            setattr(obj, name, value)
            return
    raise TypeError("can't add new attribute")
