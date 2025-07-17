#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """This class defines a square with a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value checks).
        """
        self.__size = size
