#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is a positive integer"""
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the Rectangle instance with width and height"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
