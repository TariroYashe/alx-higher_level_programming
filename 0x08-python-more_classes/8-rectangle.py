#!/usr/bin/python3
"""Defines a Rectangle class."""
# Importantly, this comment at the top describes the purpose of the code file.

class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """
    # This is a docstring for the Rectangle class, describing its purpose and attributes.

    number_of_instances = 0
    print_symbol = "#"  # Default print symbol is #

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        # This docstring describes the constructor of the class.
        type(self).number_of_instances += 1  # Increment the count of instances.
        self.width = width  # Set the width
        self.height = height  # Set the height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width
        # Property to get the width attribute

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        # Property to set the width attribute with type and value validation.

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height
        # Property to get the height attribute

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        # Property to set the height attribute with type and value validation.

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)
        # Calculate and return the area of the rectangle.

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
        # Calculate and return the perimeter of the rectangle.

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        # This is a static method to compare two rectangles and return the one with a greater area.
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        # This method returns a string representation of the rectangle using '#' symbols.
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        # This method returns a string representation of the rectangle object.
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        # This method is called when a rectangle instance is deleted.
        type(self).number_of_instances -= 1
        print("Bye rectangle...")