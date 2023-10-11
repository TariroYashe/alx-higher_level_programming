#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_to_set_1 = set_1.difference(set_2)
    unique_to_set_2 = set_2.difference(set_1)
    return unique_to_set_1.union(unique_to_set_2)
