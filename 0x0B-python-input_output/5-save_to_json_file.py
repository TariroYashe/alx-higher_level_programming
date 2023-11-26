#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json

def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj (Any): The object to be serialized and written to the file.
        filename (str): The name of the file to write the JSON data to.
    """
    # Open the file in write mode and use 'with' to ensure proper file closure
    with open(filename, "w") as file:
        # Use the json.dump function to serialize the object and write it to the file
        json.dump(my_obj, file)
