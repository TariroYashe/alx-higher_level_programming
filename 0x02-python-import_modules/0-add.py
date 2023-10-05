#!/usr/bin/python3

# Check if the script is being run as the main program.
if __name__ == "__main__":
    """Print the sum of 1 and 2."""

    # Import the 'add' function from the 'add_0' module.
    from add_0 import add

    # Define two variables, 'a' and 'b', and assign them the values 1 and 2.
    a = 1
    b = 2

    # Calculate the sum of 'a'& 'b' using the 'add' func and print the result
    print("{} + {} = {}".format(a, b, add(a, b)))
