#!/usr/bin/env python3
import csv
import math
from typing import List

"""Simple pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for
    those particular pagination parameters."""
    # Caluclate the start of the index of current page
    start_index = (page - 1) * page_size
    # Caluclate the end " "
    end_index = start_index + page_size

    return start_index, end_index


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
        """Return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0, "page must be pos int"
        assert isinstance(page_size, int) and page_size > 0, "page_size ("")"

        """Find start and end indices using prev function (index_range)"""
        start_index, end_index = index_range(page, page_size)

        """Retrieves the dataset"""
        dataset = self.dataset()

        """Return correct page of dataset based on start and end"""
        return dataset[start_index:end_index]
