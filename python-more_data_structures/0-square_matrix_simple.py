#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square of all integers in a 2D matrix.

    Args:
        matrix (list of lists of int): 2D matrix of integers.

    Returns:
        list of lists of int: New matrix with squared values.
    """
    return [[x ** 2 for x in row] for row in matrix]
