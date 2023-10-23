#!/usr/bin/python3

def magic_calculation(a, b):
    # Initialize the result variable
    result = 0

    # Iterate over a range from 1 to 3
    for i in range(1, 4):
        try:
            # Check if i is greater than a
            if i > a:
                # Raise an exception with the message 'Too far'
                raise Exception('Too far')

            # Perform some mathematical operations
            result += (a ** b) / i
        except Exception:
            # Handle the exception by setting the result to b + a
            result = b + a
            break

    # Return the final result
    return result
