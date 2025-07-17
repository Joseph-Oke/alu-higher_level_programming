#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element 2 lists, handling exceptions.

    Args:
        my_list_1 (list): First list.
        my_list_2 (list): Second list.
        list_length (int): Number of elements to divide.

    Returns:
        list: New list with results of division.
    """
    new_list = []
    for i in range(list_length):
        try:
