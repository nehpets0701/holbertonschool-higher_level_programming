#!/usr/bin/python3
"""divides a matrix"""


def matrix_divided(matrix, div):
    """divides a matrix"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        matrixlength = len(matrix[0])
    for x in range(len(matrix)):
        if type(matrix[x]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[x]) != matrixlength:
            raise TypeError("Each row of the matrix must have the same size")
        for y in range(len(matrix[x])):
            if type(matrix[x][y]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    for row in matrix:
        new.append(list(map(lambda x: round(x / div, 2), row)))
    return new
