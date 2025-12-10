#!/usr/bin/python3
class Square:
    """
    Defines a square by its size.
    The size is stored as a private instance attribute: __size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size: The size of one side of the square. 
                  (No type or value verification is performed.)
        """
        # Private instance attribute '__size' is set here. 
        # The double underscore invokes name mangling in Python.
        self.__size = size
