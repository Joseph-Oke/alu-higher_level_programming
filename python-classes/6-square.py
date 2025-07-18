#!/usr/bin/python3
"""Defines a Square class with size and position properties."""


class Square:
    """Square class with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): Size of the square (default 0).
            position (tuple): Position for printing (default (0, 0)).

        Raises:
            TypeError: If size is not int or position is not a tuple of
                2 positive integers.
            ValueError: If size < 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # taking position into account."""
        if self.__size == 0:
            print()
            return

        # print the vertical offset
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            # print the horizontal offset spaces, then the #
            print(" " * self.__position[0] + "#" * self.__size)
