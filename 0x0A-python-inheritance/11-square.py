#!/usr/bin/python3
"""This module defines a Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init(size, size)
        self.__size = size
