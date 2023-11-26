#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    """
    Print the contents of a UTF-8 text file to stdout.

    Parameters:
    - filename (str): The path to the text file to be read. Default is an empty string.
    """
    # Open the specified file in UTF-8 encoding using a 'with' statement
    with open(filename, encoding="utf-8") as f:
        # Read the contents of the file and print them to stdout
        print(f.read(), end="")
