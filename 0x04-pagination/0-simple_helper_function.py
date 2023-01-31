#!/usr/bin/env python3
""" function named index_range that takes two integer arguments
page and page_size return a tuple of size two containing a start index
and an end index """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Simple helper function
    """
    s_index = (page - 1) * page_size
    e_index = s_index + page_size
    return (s_index, e_index)
