#!/usr/bin/python3
"""
method module
"""


def add_attribute(obj, a, v):
        """add attribute to object
    args:
        obj: class object
        objname: object name
        value: value of attribute
    return:
        na
    """
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")
