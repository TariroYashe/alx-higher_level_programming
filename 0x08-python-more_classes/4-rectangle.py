#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        # Initialize the Rectangle with the specified width and height.
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        # Getter method for retrieving the width of the Rectangle.
        return self.__width

    @width.setter
    def width(self, value):
        # Setter method for setting the width of the Rectangle.
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        # Ensure the width is a non-negative integer.
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        # Getter method for retrieving the height of the Rectangle.
        return self.__height

    @height.setter
    def height(self, value):
        # Setter method for setting the height of the Rectangle.
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        # Ensure the height is a non-negative integer.

        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        # Calculate and return the area of the Rectangle.
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        # Calculate and return the perimeter of the Rectangle.
        if self.__width == 0 or self.__height == 0:
            return (0)
        # If either width or height is zero, the perimeter is zero.
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        # Create a string representation of the Rectangle using '#'.
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        # Return a string representation that can be used to recreate the Rectangle.
        return (rect)