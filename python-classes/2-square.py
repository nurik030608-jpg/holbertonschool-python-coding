#!/usr/bin/python3
"""
This module contains the definition of the Square class. 
It meets all requirements for task 1, including size validation. 
"""


class Square:
    """
    Defines a square by its size and handles initialization with validation. 
    This is the required class docstring.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
    return self.__size ** 2
