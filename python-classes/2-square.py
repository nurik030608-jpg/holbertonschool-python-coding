#!/usr/bin/python3
"""
Module 2-square: Defines a Square class with private size attribute,
validation, and a public area calculation method.
"""


class Square:
    """
    Defines a square by its size.

    Attributes:
        __size (int): The size (side length) of the square, a private attribute.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with optional size and validation.
        
        Args:
            size (int, optional): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        # The body of the method must be indented
        return self.__size ** 2
