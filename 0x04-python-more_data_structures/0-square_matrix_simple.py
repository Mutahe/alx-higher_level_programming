#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for line in matrix:
        new_matrix.append([t**2 for t in line])
    return new_matrix
