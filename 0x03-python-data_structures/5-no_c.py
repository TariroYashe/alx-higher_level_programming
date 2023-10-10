#!/usr/bin/env python3
def no_c(my_string):
    # Initialize an empty string to store the result
    result = ""

    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is not 'c' or 'C'
        if char != 'c' and char != 'C':
            # If it's not 'c' or 'C', add it to the result string
            result += char

    return result
