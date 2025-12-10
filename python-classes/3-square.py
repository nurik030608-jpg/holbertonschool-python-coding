#!/usr/bin/python3
"""
Module 3-square: Defines a Square class with private size attribute, 
using a property (getter and setter) for robust validation and access.
"""


class Square:
    """
    Defines a square by its size.

    Attributes:
        __size (int): The size (side length) of the square, a private attribute.
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with optional size.
        
        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
            The setter method is used internally for validation.
        """
        # The setter method is called here to handle validation during instantiation
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        
        Returns:
            int: The size (side length) of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with type and value validation.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
            
        self.__size = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
