#!/usr/bin/python3

# Define a class named Rectangle.
class Rectangle:
    # Class-level attributes (class variables) for all instances of the class.
    # `number_of_instances` keeps track of the number of instances.
    # `print_symbol` is used for customizing the string representation of the rectangle.
    number_of_instances = 0
    print_symbol = "#"

    # Constructor method to initialize a new Rectangle instance.
    def __init__(self, width=0, height=0):
        # Increase the count of instances each time a new instance is created.
        type(self).number_of_instances += 1
        # Use properties to set the width and height attributes.
        self.width = width
        self.height = height

    # Property method for getting and setting the 'width' attribute.
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Check if 'width' is an integer; raise an error if it's not.
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        # Check if 'width' is non-negative; raise an error if it's negative.
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Property method for getting and setting the 'height' attribute.
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        # Check if 'height' is an integer; raise an error if it's not.
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        # Check if 'height' is non-negative; raise an error if it's negative.
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Method to calculate and return the area of the Rectangle.
    def area(self):
        return (self.__width * self.__height)

    # Method to calculate and return the perimeter of the Rectangle.
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)

    # Method for generating a string representation of the Rectangle.
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    # Method to generate a string representation of the Rectangle for use with eval().
    def __repr__(self):
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    # Destructor method, called when a Rectangle instance is deleted.
    def __del__(self):
        # Decrease the count of instances upon deletion.
        type(self).number_of_instances -= 1
        print("Bye rectangle...")