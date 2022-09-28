#!/usr/python3
""" module contains function that Returns an object
represented by a json string
"""
import json


def from_json_string(my_str):
        """ Function that Returns an object representation of a json string
        Args:
             my_str: Json representation
        Raise:
             Exception: when the string can't be decode
        """
        return json.loads(my_str)
