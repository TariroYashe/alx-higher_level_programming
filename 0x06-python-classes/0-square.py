#!/usr/bin/python3

class Square:
    """
    This class defines a square.

    The Sqre class is used to represent a sqre shape. It can be instantiated
    to create square objects, and provides methods and attributes for working
    with squares.

    Attributes:
        side_length (int): The length of each side of the square.

    Methods:
        __init__(self, side_length): Initializes a sqre wth the given side len
        area(self): Computes and returns the area of the square.
    """

    def __init__(self, side_length=0):
        """
        Initializes a square with the given side length.

        Args:
            side_length (int): The length of each side of the square.
        """
        self.side_length = side_length

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.side_length ** 2
