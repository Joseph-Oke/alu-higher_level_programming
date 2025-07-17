#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys (only first level keys).

    Args:
        a_dictionary (dict): Dictionary with string keys.
    """
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
