#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    '''Check if the key exists in the dictionary'''
    if key in a_dictionary:
        '''If it exists, del the key and its corresponding value'''
        del a_dictionary[key]
    return a_dictionary
