#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json

def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Parameters:
    - filename (str): The name of the JSON file to read.

    Returns:
    - dict or list: The Python object created from the JSON file.
    """
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Load the JSON data from the file into a Python object
            data = json.load(file)
        return data
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        # Handle the case where the JSON decoding fails
        print(f"Error: Failed to decode JSON in file '{filename}'.")
        return None
    