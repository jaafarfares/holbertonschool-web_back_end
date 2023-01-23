#!/usr/bin/env python3
"""
This file contains various functions with type hints.
Functions perform different operations on input data and return result.
All functions have been annotated with type hints.
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    This function takes a list and an optional integer factor as input and
    returns a new list containing the elements of the original list repeated
    factor number of times. """
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
