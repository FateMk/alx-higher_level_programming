#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemeted")
    def integer_validator(self, name, value):
        if type(value) if not int:
            raise TypeError("<name> must be an integer")
        if (value[] <= 0):
            raise ValueError("<name> must be greater than 0")
