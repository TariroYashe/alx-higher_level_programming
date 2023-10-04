#!/usr/bin/python3

def uppercase(input_str):
    """Print a string in uppercase."""
    result = ""
    
    for char in input_str:
        if 'a' <= char <= 'z':
            # Convert lowercase character to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            result += uppercase_char
        else:
            result += char
    
    print(result)
