#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Replace or add key/value in a dictionary.

    Args:
        a_dictionary (dict): Dictionary to update.
        key (str): Key to replace or add.
        value: Value associated with the key.

    Returns:
        dict: Updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
