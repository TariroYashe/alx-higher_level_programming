#!/usr/bin/python3

# Check if the script is being run as the main program.
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""

    # Import the add, sub, mul, and div func from the 'calculator_1' module.
    from calculator_1 import add, sub, mul, div

    # Define two variables, 'a' and 'b', and assign them the values 10 and 5.
    a = 10
    b = 5

    # Calculate and print the sum of 'a' and 'b' using the 'add' func
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Calculate and print the difference of 'a' and 'b' using the 'sub' func
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Calculate and print the product of 'a' and 'b' using the 'mul' func
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Calculate and print the quotient of 'a' and 'b' using the 'div' func
    print("{} / {} = {}".format(a, b, div(a, b)))
