#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize an empty list to store True/False values
    result_list = []

    # Iterate through each element in the input list
    for num in my_list:
        # Check if the number is divisible by 2 (i.e., even)
        if num % 2 == 0:
            result_list.append(True)
        else:
            result_list.append(False)

    return result_list
