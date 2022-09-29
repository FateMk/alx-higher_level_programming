#!/usr/bin/pyhton3
"""contains class Square subclass of Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square"""
    def __init__(self, size):
        """initilization"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """prints square description"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
