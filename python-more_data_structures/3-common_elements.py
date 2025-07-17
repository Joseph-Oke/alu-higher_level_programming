#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Return a set of common elements in two sets.

    Args:
        set_1 (set): First set.
        set_2 (set): Second set.

    Returns:
        set: Set of elements common to both.
    """
    common = set()
    for elem in set_1:
        if elem in set_2:
            common.add(elem)
    return common
