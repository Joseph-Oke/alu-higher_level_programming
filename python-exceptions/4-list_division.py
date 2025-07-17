#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divide elements of 2 lists element by element.

    Args:
        my_list_1 (list): First list.
        my_list_2 (list): Second list.
        list_length (int): Number of elements to divide.

    Returns:
        list: New list with division results.
    """
    result_list = []
    for i in range(list_length):
        result = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            result = a / b
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            result_list.append(result)
    return result_list
