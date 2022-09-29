#!/usr/bin/python3
"""defining class Student"""


class Student:
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
     def reload_from_json(self, json):
        """reloads Student instance from input dictionary"""
        for k, v in json.items():
            setattr(self, k, v)
