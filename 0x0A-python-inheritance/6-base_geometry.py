#!/usr/bin/python3
class BaseGeometry:
    """
    BaseGeometry class with an area() method that raises an Exception.
    """

    def area(self):
        """
        Raise an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
    