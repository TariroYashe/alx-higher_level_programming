#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed = 0  # Initialize a var to count the number of elems printed
        for i in range(x):  # Loop up to x
            print(my_list[i], end=" ")  # Print the element without a newline
            printed += 1  # Increment the count of elements printed
        print()  # Print a newline after all elements
        return printed  # Return the number of elements actually printed
    except IndexError:
        print()  # Print a /n when an IndexError is caught (x > len of my_list)
        return printed  # Return the number of elements actually printed
