#!/usr/bin/env python3
"""
This file contains various functions with type hints.
Functions perform different operations on input data and return result.
All functions have been annotated with type hints.
"""
import typing


def zoom_array(lst: tuple, factor: int = 2) -> list:
    """_summary_

    Args:
        lst (tuple): _description_
        factor (int, optional): _description_. Defaults to 2.

    Returns:
        list: _description_
    """
    zoomed_in: list = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
