#!/usr/bin/python3
"""Module defining BaseGeometry class with unimplemented area method."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
