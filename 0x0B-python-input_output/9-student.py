#!/usr/bin/python3
"""defining class Student"""


class Student:
    """class that creates a student instance"""
    def __init__(self, first_name, last_name, age):
        """initializing new instance of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self):
        """ Method that returns directory description """
        return self.__dict__.copy()
