#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import++('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
