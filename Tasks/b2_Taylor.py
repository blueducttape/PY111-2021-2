"""
Taylor series
"""
from typing import Union
from itertools import count
import math


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    exp = 1
    EPSILON = 0.0001  # точность подсчета
    for n in count(1,1):
        cur_exp = (x ** n) / math.factorial(n)
        exp += cur_exp
        if EPSILON > cur_exp:
            break
    return exp


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sin_x = 0
    EPSILON = 0.0001
    for n in count(0, 1):
        sin_x_n = (((-1) ** n) / math.factorial((2 * n) + 1)) * (x ** ((2 * n) + 1))
        sin_x += sin_x_n
        if abs(sin_x_n) < EPSILON:
            break
    return sin_x
    # (((-1) ** n) / math.factorial((2 * n) + 1)) * (x ** ((2 * n) + 1))

    print(x)
    return 0
