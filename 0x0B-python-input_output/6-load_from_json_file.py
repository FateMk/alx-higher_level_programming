#!/usr/bin/python3
"""Module contains a function that creates an 
Object from a “JSON file"
"""
import json


def load_from_json_file(filename):
    """Function that creates an object from JSON file
    Args:
        filaname: JSON representation
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
