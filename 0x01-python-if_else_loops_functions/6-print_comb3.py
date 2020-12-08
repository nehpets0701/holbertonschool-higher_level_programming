#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if y > x and x != 8:
            print("{:d}{:d}, ".format(x, y), end="")
        elif y > x:
            print("89")
