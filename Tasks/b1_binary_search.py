from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    left = 0
    right = len(arr) - 1

    while left <= right:

        middle = (left + right) // 2

        if arr[middle] == elem:
            return middle
        elif arr[middle] > elem:
            right = middle - 1
        else:
            left = middle + 1

    return None
