#!/usr/bin/python3
"""Defines a Square class with size property, area, and printing methods."""


class Square:
    """Square class with size property, area calculation, and printing."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): Size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # uses the setter for validation

    @property
    def size(self):
        """Get the current size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): New size value.

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
        """Calculate the current square area.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' to stdout.

        Prints an empty line if size is 0.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
