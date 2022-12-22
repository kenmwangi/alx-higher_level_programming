#!/usr/bin/python3
""" Matrix divided method"""

def matrix_divided(matrix, div):
    """Divide all elements of matrix

    args: elements divided by div

    Errors

    TypeError - if matrix not a list of lists(int, float)
    TypeError - each row of matrix not same
    TypeError - div neither int or float
    ZeroDivisionError - div is zero

    Returns -  new matrix with elements rounded to 2 decimal places
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("Matrix must be a matrix (list of lists) " + "of integers/floats")
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " + "of integers/floats")

    len_rows = []
    for row in maxtrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the maxtri must have same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]
    return new_matrix
