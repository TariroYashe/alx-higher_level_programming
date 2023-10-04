#!/usr/bin/python3

def magic_calculation(a, b, c):

    # Check if 'a' is less than 'b'
    if a < b:
        # If 'a' is less than 'b', return the value of 'c'
        return (c)
    # Check if 'c' is greater than 'b'
    if c > b:
        # If 'c' is greater than 'b', return the sum of 'a' and 'b'
        return (a + b)

    # If none of the above conditions are met, return the result
    # of 'a' multiplied by 'b' minus 'c'
    return (a * b - c)
