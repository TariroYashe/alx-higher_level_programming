#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Add two integers.

    This function takes two arguments, a and b, and returns their sum as an integer.

    :param a: The first integer or float.
    :param b: The second integer or float (default is 98).
    :return: The addition of a and b as an integer.
    :raises TypeError: If either a or b is not an integer or float.

    Usage:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    """
    if (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)):
        a = int(a) if isinstance(a, float) else a
        b = int(b) if isinstance(b, float) else b
        return int(a + b)
    else:
        raise TypeError("a must be an integer or b must be an integer")
