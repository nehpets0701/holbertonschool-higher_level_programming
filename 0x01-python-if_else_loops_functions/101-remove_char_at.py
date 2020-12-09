#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    index = 0
    for x in str:
        if (index != n):
            new += x
        index += 1
    return new
