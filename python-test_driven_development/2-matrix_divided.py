#!/usr/bin/python3
"""This module defines a matrix_divided function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div, rounded to 2 decimals"""
    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix) or
            not all(
                isinstance(n, (int, float)) and not isinstance(n, bool)
                for row in matrix for n in row
            )):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(n / div, 2) for n in row] for row in matrix]
