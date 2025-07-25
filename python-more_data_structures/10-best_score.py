#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value in a dictionary.

    Args:
        a_dictionary (dict): Dictionary with string keys and integer values.

    Returns:
        key with the highest value or None if dictionary is empty or None.
    """
    if not a_dictionary:
        return None

    best_key = None
    best_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key
