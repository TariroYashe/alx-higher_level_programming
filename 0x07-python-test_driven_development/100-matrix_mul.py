#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): The first matrix to be multiplied.
        m_b (list of lists): The second matrix to be multiplied.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        ValueError: If the matrices can't be multiplied.
        TypeError: If the input matrices are not in the correct format.

    Example:
        >>> matrix_A = [[1, 2], [3, 4]]
        >>> matrix_B = [[1, 2], [3, 4]]
        >>> result_matrix = matrix_mul(matrix_A, matrix_B)
        >>> result_matrix
        [[7, 10], [15, 22]]
    """
    def matrix_mul(m_a, m_b):
    # Requirement 1: Check if m_a and m_b are not empty
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    # Requirement 2: Check if the number of columns in m_a equals the number of rows in m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("Matrix dimensions are not suitable for multiplication")

    # Requirement 3: Check if m_a and m_b are lists of lists of integers or floats
    for matrix in [m_a, m_b]:
        if not isinstance(matrix, (list, tuple)) or not all(isinstance(row, (list, tuple)) for row in matrix):
            raise TypeError(f"{matrix} must be a list of lists or tuples")
        row_size = len(matrix[0])
        for row in matrix:
            if not all(isinstance(element, (int, float)) for element in row):
                raise TypeError(f"{matrix} should contain only integers or floats")
            if len(row) != row_size:
                raise TypeError(f"Each row of {matrix} must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Create an empty result matrix with the appropriate dimensions
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Perform matrix multiplication
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result