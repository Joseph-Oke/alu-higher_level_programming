#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of 'search' by 'replace' in a new list.

    Args:
        my_list (list): Original list.
        search: Element to replace.
        replace: New element to put instead.

    Returns:
        list: New list with replacements.
    """
    return [replace if x == search else x for x in my_list]
