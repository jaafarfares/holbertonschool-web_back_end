#!/usr/bin/env python3
"""type-annotated function to_kv that takes a string k and an int OR float
v as arguments and returns a tuple"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """pass the first element as str and multiply the others"""
    if isinstance(v, int):
        v = float(v)
    square: tuple[str, float] = (k, v*v)
    return square
