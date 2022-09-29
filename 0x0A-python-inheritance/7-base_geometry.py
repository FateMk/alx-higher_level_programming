#!/usr/bin/python3
"""defining class BaseGoemetry"""


class BaseGeometry:
    """A class with public attributes"""
    def area(self):
        """raises an exception ehen called"""
        raise Exception("area() is not implemeted")
        
    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) if not int:
            raise TypeError("<name> must be an integer")
        if (value[] <= 0):
            raise ValueError("<name> must be greater than 0")
