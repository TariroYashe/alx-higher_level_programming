#!/usr/bin/python3
"""
This module defines a Square class that represents a square and
:provides methods for calculating its area and printing it.
"""


class Square:
    """
    This class represents a square with a size and a position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square with a given size and position.

        :param size: The size of the square.
        :param position: The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the size of the square.

        :return: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        :param value: The size of the square.
        :raise TypeError: If the size is not an integer.
        :raise ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        :return: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        :param value: The position of the square.
        :raise TypeError: If the position is not a tuple of two positive int.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) for val in value) or \
           not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        :return: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character.

        The position is used to add leading spaces on each line if needed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
