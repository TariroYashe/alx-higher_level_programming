#!/usr/bin/python3

# Check if this script is being run as the main program
if __name__ == '__main__':
    # Import functions add, sub, mul, and div from calculator_1 module
    from calculator_1 import add, sub, mul, div
    
    # Define two numbers for calculation
    a = 10
    b = 5
    
    # Perform addition and print the result
    print("{} + {} = {}".format(a, b, add(a, b)))
    
    # Perform subtraction and print the result
    print("{} - {} = {}".format(a, b, sub(a, b)))
    
    # Perform multiplication and print the result
    print("{} * {} = {}".format(a, b, mul(a, b)))
    
    # Perform division and print the result
    print("{} / {} = {}".format(a, b, div(a, b)))
