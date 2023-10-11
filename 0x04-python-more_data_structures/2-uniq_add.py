#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Create an empty set to store unique integers"""
    unique_integers = set()
    """Initialize a variable to store the sum of unique integers"""
    total = 0

    for num in my_list:
        """Check if the current num 'num' is not in the 'unique_int' set"""
        if num not in unique_integers:
            total += num
            unique_integers.add(num)

    return total
