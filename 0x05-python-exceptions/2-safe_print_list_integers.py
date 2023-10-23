#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Init  a count to keep track of the number of int printed
    try:
        for item in my_list:
            if x == 0:
                break  # Stop if we have printed the required number of int

            try:
                if isinstance(item, int):
                    print("{:d}".format(item), end=" ")  # Print the integer
                    count += 1
                x -= 1  # Decrease the count of elements to print
            except ValueError:
                pass  # Ignore non-integer values
    except Exception:
        pass  # Ignore exceptions if x is greater than the length of my_list

    print()  # Print a newline after all integers have been printed
    return count
