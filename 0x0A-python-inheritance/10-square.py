#!/usr/bin/python3
"""contains class Square a subclass of Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of Square"""
    def __init__(self, size):
        """initilization"""
        super().__init__(size, size)
