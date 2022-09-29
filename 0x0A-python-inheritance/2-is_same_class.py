#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_sane_class(obj, a_class):
    """returns True if the object is exactly a class otherwise False"""
    return (obj.__class__ == a_class)
