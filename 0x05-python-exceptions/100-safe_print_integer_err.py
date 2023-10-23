#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        # Try to format the value as an integer and print it
        formatted_value = "{:d}".format(value)
        print(formatted_value)
        return True
    except (ValueError, TypeError):
        # Catch exceptions for non-integer values
        error_message = "Exception: {} is not an integer".format(value)
        print(error_message, file=sys.stderr)
        return False
