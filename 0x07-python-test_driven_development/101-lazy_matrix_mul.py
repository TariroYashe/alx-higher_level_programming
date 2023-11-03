#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): The first matrix as a list of lists.
        m_b (list): The second matrix as a list of lists.

    Returns:
        numpy.ndarray: The product of the two matrices as a NumPy array.

    Raises:
        ValueError: If the matrices cannot be multiplied due to incompatible shapes.

    This function takes two matrices as input and returns their product using NumPy's dot product operation.
    It checks for compatibility of matrix dimensions and raises a ValueError if they cannot be multiplied.
    """
    try:
        result = np.dot(np.array(m_a), np.array(m_b))
        return result
    except ValueError as e:
        raise ValueError("NumPy dot error: " + str(e))
    except Exception as e:
        raise e