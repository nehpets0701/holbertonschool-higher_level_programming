#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for x in range(len(matrix)):
        new.append(list(map(lambda x: x * x, matrix[x])))
    return new
