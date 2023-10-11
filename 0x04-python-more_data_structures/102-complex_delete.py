#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a copy of the original dictionary to avoid modifying it directly
    new_dict = a_dictionary.copy()

    # Iterate over the keys and values in the dictionary
    for key, val in a_dictionary.items():
        if val == value:
            # If the value matches the specified value, del key from the copy
            del new_dict[key]

    return new_dict
