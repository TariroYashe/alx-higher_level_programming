#!/usr/bin/python3
"""Defines a Rectangle class."""

# Define a class named Rectangle
class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    # Class attribute to keep track of the number of instances created
    number_of_instances = 0

    # Constructor method to initialize a new Rectangle instance
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        # Increment the number of instances
        type(self).number_of_instances += 1

        # Initialize width and height instance attributes
        self.width = width
        self.height = height

    # Getter and setter methods for the width attribute
    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        # Check if the value is an integer
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        # Check if the value is non-negative
        if value < 0:
            raise ValueError("width must be >= 0")

        # Set the width attribute
        self.__width = value

    # Getter and setter methods for the height attribute
    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        # Check if the value is an integer
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        # Check if the value is non-negative
        if value < 0:
            raise ValueError("height must be >= 0")

        # Set the height attribute
        self.__height = value

    # Method to calculate and return the area of the Rectangle
    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    # Method to calculate and return the perimeter of the Rectangle
    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    # Method to return a printable representation of the Rectangle
    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            # Add '#' characters to the rectangle
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")  # Add newline character if not the last row
        return ("".join(rect))  # Join the characters into a string

    # Method to return a string representation of the Rectangle
    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    # Method to handle the deletion of a Rectangle instance
    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        # Decrement the number of instances
        type(self).number_of_instances -= 1
        print("Bye rectangle...")  # Print a message when an instance is deleted