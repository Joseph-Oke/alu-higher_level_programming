#!/usr/bin/python3
def safe_print_division(a, b):
    """Divide two integers and print the result inside finally.

    Args:
        a (int): Numerator.
        b (int): Denominator.

    Returns:
        The result of the division or None if division by zero.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        r
