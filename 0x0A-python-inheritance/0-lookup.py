#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Args:
        obj: The object for which to list attributes and methods.

    Returns:
        A list of attribute and method names.
    """
    return [attr for attr in dir(obj) if not attr.startswith("__")]
