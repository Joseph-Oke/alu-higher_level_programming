#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer using '{:d}'.format() safely.

    Args:
        value: Any type.

    Returns:
        bool: True if value is integer and printed, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
