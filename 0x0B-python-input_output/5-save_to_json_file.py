#!/urs/bin/python3
""" module contains a function that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Functin writes an object to text file in JSON
    Args:
        my_obj: object
        filename: textfile name
    Raises:
        Exception: when the string can't be decoded
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(obj))
