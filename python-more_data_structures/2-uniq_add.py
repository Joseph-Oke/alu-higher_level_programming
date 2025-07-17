#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer).

    Args:
        my_list (list): List of integers.

    Returns:
        int: Sum of unique integers.
    """
    unique_elements = []
    for num in my_list:
        if num not in unique_elements:
            unique_elements.append(num)
    return sum(unique_elements)
