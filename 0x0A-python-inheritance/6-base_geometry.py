#!/usr/bin/python3
"""defining class BaseGeometry"""


class BaseGeometry:
    """A class with public attributes"""
    
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
