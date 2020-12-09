#!/usr/bin/python3
for c in reversed(range(ord('a'), ord('z') + 1)):
    if c % 2 != 0:
        char = c - 32
    else:
        char = c
    print("{:c}".format(char), end="")
