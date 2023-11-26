#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json

def to_json_string(my_obj):
    """
    Return the JSON representation of a Python object.

    Parameters:
    - my_obj: The Python object to be converted to JSON.

    Returns:
    A JSON-formatted string representing the input object.
    """
    # Use the json.dumps() method to convert the Python object to a JSON string
    json_string = json.dumps(my_obj)
    
    # Return the resulting JSON string
    return json_string
