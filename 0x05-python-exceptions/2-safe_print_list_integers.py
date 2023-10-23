#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            item = my_list[i]
            if isinstance(item, int):
                print("{:d}".format(item), end='')
                count += 1
    except IndexError:  # Catch IndexError separately
        pass

    print()  # Print a newline after all integers are printed
    return count
