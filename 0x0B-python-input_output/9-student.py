#!/usr/bin/python3
"""defining class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initializing new instance of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        """returns dict attributes of student"""
        try:
            obj_dict = self._dict_
            return obj_dict
        except:
            return {}

