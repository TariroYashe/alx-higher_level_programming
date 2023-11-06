#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.

    :param obj: The object to check.
    :param a_class: The class to check for inheritance.
    :return: True if obj is an instance of a class inherited from a_class, otherwise False.
    """
    return issubclass(type(obj), a_class)
