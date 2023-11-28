#!/usr?bin/python3

"""divides all elements of a matrix."""

def matrix_divided(matrix, div):
    """matrix must be a list of lists of integers or floats, otherwise raise a TypeError.
    Each row of the matrix must be of the same size, otherwise raise a TypeError.
    div must be a number (integer or float), otherwise raise a TypeError.
    div can’t be equal to 0, otherwise raise a ZeroDivisionError.
    All elements of the matrix should be divided by div, rounded to 2 decimal places.
    Returns a new matrix.
    """
