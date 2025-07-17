#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set.

    Args:
        set_1 (set): First set.
        set_2 (set): Second set.

    Returns:
        set: Elements present in set_1 or set_2 but not both.
    """
    diff = set()
    for elem in set_1:
        if elem not in set_2:
            diff.add(elem)
    for elem in set_2:
        if elem not in set_1:
            diff.add(elem)
    return diff
