#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elem by ext with 0 if necessary
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Take only the first 2 of each tuple and add them element-wise
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple
