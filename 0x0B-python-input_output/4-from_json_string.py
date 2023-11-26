#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-object function."""

import json

def from_json_string(json_string):
    """
    Convert a JSON-formatted string to a Python object.

    Parameters:
    - json_string (str): The input JSON string.

    Returns:
    - The corresponding Python object.
    """
    # Use json.loads to parse the JSON string and convert it to a Python object
    python_object = json.loads(json_string)

    # Return the resulting Python object
    return python_object
