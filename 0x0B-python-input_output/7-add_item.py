#!/usr/bin/python3
"""
Add all command line arguments to a Python list and save them to a JSON file.
"""
import sys
import json

def save_to_json_file(data, filename):
    """
    Save data to a JSON file.

    Args:
        data: The data to be saved.
        filename: The name of the file to save the data to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_from_json_file(filename):
    """
    Load data from a JSON file.

    Args:
        filename: The name of the file to load data from.

    Returns:
        The loaded data.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    