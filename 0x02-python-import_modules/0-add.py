#!/usr/bin/python3
# Define the add function (you can only use the word add_0 once)
def add(a, b):
    return a + b
if __name__ == "__main__":
    # Assign values to variables a and b
    a = 1
    b = 2

    # Calculate the sum using the add function
    result = add(a, b)

    # Print the result using string formatting
    print("{} + {} = {}".format(a, b, result))
