#!/usr/bin/python3
"""defining class Student"""


class Student:
     """ Class to create student instances """
        
    def __init__(self, first_name, last_name, age):
        """initializing new instance of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        """returns dict attributes of student"""
        if attrs is None:
            obj_dict = sef.__dict__
            return obj_dict
        else:
            all_t = self.__dict__
            D = dict(([k, v] for k, v in all_t.items() if k in attrs))
            return D
