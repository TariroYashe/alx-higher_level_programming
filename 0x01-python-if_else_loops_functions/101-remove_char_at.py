#!/usr/bin/python3

# Define a function called remove_char_at that takes two parameters:
# - str: the input string
# - n: the position of the character to remove
def remove_char_at(str, n):
    # Check if the given position (n) is negative
    if n < 0:
        # If n is negative, return the original string unchanged
        return (str)
    # If n is non-negative (greater than or equal to 0), create a
    # new strngby concatenating two slices of the input string:
    # - str[:n] rep the part of the string before the char at position n
    # - str[n+1:] rep the part of the strng after the char at position n
    # This effectively removes the character at position n.
    return (str[:n] + str[n+1:])
