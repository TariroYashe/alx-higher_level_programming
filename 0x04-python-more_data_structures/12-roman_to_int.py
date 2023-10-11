#!/usr/bin/python3
def roman_to_int(roman_string):
    '''Check if the input is a string and not None'''
    if not isinstance(roman_string, str) or roman_string is None:
        return 0    #Return 0 for invalid input

    '''Def a dictionary to map Roman numerals to their int values'''
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    '''Initialize the result and a var to keep track of the prev value'''
    result = 0
    prev_value = 0

    '''Iterate through the Roman numeral string in reverse order'''
    for char in reversed(roman_string):
        '''Check if the character is a valid Roman numeral'''
        if char not in roman_numerals:
            return 0    #Return 0 for invalid Roman numeral character

        '''Get the integer value for the current character'''
        value = roman_numerals[char]

        '''Compthe current value with the prev value to apply subtrct rule'''
        if value < prev_value:
            result -= value
        else:
            result += value

        '''Update the previous value for the next iteration'''
        prev_value = value

    '''Return the final calculated result'''
    return result
