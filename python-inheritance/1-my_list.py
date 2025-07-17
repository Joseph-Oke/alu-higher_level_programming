#!/usr/bin/python3
"""Module defining MyList class inherited from list."""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
