#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Initialize a new list to store the result
    new_list = []

    # Iterate through the original list and skip the item at idx
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    return new_list
