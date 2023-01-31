#!/usr/bin/env python3
""" function named index_range that takes two integer arguments
page and page_size return a tuple of size two containing a start index
and an end index """
from typing import Tuple, List
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method to return the rows from the dataset in the specified page.
        Parameters:
        page (int): Page number, default value is 1.
        page_size (int): Number of rows per page, default value is 10.
        Returns:
        List[List]: List of rows of the specified page. If page number is out
        of range, an empty list is returned.
        Raises:
        AssertionError: If either `page` or `page_size` is not an integer
        greater than 0. """
        assert isinstance(
            page, int) and page > 0,
        assert isinstance(
            page_size, int) and page_size > 0,
        rows = self.dataset()

        start, end = self.index_range(page, page_size)
        if start >= len(rows):
            return []
        return rows[start:end]

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Simple helper function
        """
        s_index = (page - 1) * page_size
        e_index = s_index + page_size
        return (s_index, e_index)
