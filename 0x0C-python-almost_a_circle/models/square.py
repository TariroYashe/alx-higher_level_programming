#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle  # Import the Rectangle class from the rectangle module


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)  # Call the constructor of the parent class (Rectangle)
    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width  # The size of the square is represented by the width attribute

    @size.setter
    def size(self, value):
        self.width = value  # Set the width attribute to the new size value
        self.height = value  # Set the height attribute to the new size value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)  # If id is None, reinitialize with current size, x, and y
                    else:
                        self.id = arg  # Set the id attribute to the new value
                elif a == 1:
                    self.size = arg  # Set the size attribute to the new value
                elif a == 2:
                    self.x = arg  # Set the x attribute to the new value
                elif a == 3:
                    self.y = arg  # Set the y attribute to the new value
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)  # If id is None, reinitialize with current size, x, and y
                    else:
                        self.id = v  # Set the id attribute to the new value
                elif k == "size":
                    self.size = v  # Set the size attribute to the new value
                elif k == "x":
                    self.x = v  # Set the x attribute to the new value
                elif k == "y":
                    self.y = v  # Set the y attribute to the new value
    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,       # Unique identifier for the square
            "size": self.width,  # Size of the square (assuming width is used for size)
            "x": self.x,         # x-coordinate of the square's position
            "y": self.y          # y-coordinate of the square's position
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)