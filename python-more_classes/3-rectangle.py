#!/usr/bin/python3


"""Defines a Rectangle class with printable string representation."""


class Rectangle:
    """Represents a rectangle with width and height."""

    def _init_(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def _str_(self):
        """Return the rectangle as a string of '#' characters."""
        if self._width == 0 or self._height == 0:
            return ""
        rect_lines = ["#" * self._width for _ in range(self._height)]
        return "\n".join(rect_lines)
