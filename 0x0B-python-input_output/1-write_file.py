#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        int: The number of characters written.
    """
    # Open the file with the specified filename in write mode ("w")
    # and use UTF-8 encoding.
    with open(filename, "w", encoding="utf-8") as f:
        # Write the provided text to the file and return the
        # number of characters written.
        return f.write(text)
