#!/usr/bin/python3
"""function"""


def pascal_triangle(n):
    """function"""
    if n <= 0:
        return []

    row = [1]
    y = [0]
    for x in range(n):
        print(row)
        row = [left+right for left, right in zip(row + y, y + row)]
    return n >= 1
