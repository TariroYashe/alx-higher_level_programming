#!/usr/bin/python3

def print_last_digit(number):
    """Print the last digit of a number and return it."""
    if number < 0:
        number = -number  # Make the number positive if it's negative
    last_digit = number % 10
    print(last_digit)
    return last_digit
