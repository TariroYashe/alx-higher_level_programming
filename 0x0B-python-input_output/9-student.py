#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""

def class_to_json(obj):
    """
    Return the dictionary representation of a simple data structure.

    Args:
        obj: The object for which to generate the dictionary representation.

    Returns:
        dict: A dictionary representing the object.
    """
    # Check if the object has a __dict__ attribute
    if hasattr(obj, '__dict__'):
        # Use the __dict__ attribute to get the dictionary representation
        return obj.__dict__
    else:
        # If the object does not have a __dict__ attribute, raise an exception
        raise TypeError(f"Object of type {type(obj).__name__} is not serializable to JSON.")
