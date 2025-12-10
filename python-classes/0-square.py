#!/usr/bin/python3
"""
Module 0-square: Defines a Square class.
This is the module-level docstring that the test requires.
"""
class Square:
    """
    Defines a square by its size.
    The size is stored as a private instance attribute: __size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.
        """
        self.__size = size
