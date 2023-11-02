#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number and return a new matrix.

    Args:
        matrix (list of lists of integers/floats): The input matrix.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of lists of floats: A new matrix with elements divided by div.

    Raises:
        TypeError: If the input matrix is not a list of lists of integers/floats,
                   if each row of the matrix has a different size, or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(element / div, 2) for element in row] for row in matrix]
    return result