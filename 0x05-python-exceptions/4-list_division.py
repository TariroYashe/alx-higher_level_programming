#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []  # Create an empty list to store the division results
    for i in range(list_length):
        try:
            # Check if the index is out of range for either list
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            numerator = my_list_1[i]
            denominator = my_list_2[i]

            # Check if the elements are not integers or floats
            if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
                raise TypeError("wrong type")

            # Check if the denominator is zero
            if denominator == 0:
                raise ZeroDivisionError("division by 0")

            # Perform the division and append the result to the 'result' list
            result.append(numerator / denominator)

        except IndexError as e:
            print(f"IndexError: {e}")
            result.append(0)  # Append 0 if an index is out of range
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
            result.append(0)  # Append 0 if there's a division by 0
        except TypeError as e:
            print(f"TypeError: {e}")
            result.append(0)  # Append 0 if an element is not a number
        finally:
            pass  # The 'finally' block is empty

    return result
