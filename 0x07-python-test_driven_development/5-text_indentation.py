#!/usr/bin/python3
def text_indentation(text):
    # Check if the input is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the input text based on '.', '?', and ':'
    split_chars = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in split_chars:
            lines.append(current_line)
            current_line = ""

    # Add the last line if it's not empty
    if current_line:
        lines.append(current_line)

    # Print the formatted lines with two new lines after each separator
    for line in lines:
        line = line.strip()  # Remove leading and trailing spaces
        if line:
            print(line)
            print()  # Print two new lines