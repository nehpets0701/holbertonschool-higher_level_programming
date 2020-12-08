#!/usr/bin/python3
def uppercase(str):
    s = ""
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            x = ord(x) - 32
            s += chr(x)
        else:
            s += x
    print("{:s}".format(s))
