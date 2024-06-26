#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10.
"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for
    those particular pagination parameters.

    Args:
        page: the page number
        page_size: the number of items per page

    Returns:
        tuple: A tuple containing the start and end indices
    """
    # Caluclate the start of the index of current page
    start_index = (page - 1) * page_size
    # Caluclate the end " "
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE: the path to the dataset file (csv)
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Intitalizes the server w/ dataset attr"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset

        Returns:
            List[List]: the dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset

        Args:
            page: the page number, default is 1
            page_size: the number of items per page, default is 10

        Returns:
            List[List]: the requested page of the dataset
        """
        assert isinstance(page, int) and page > 0, "page must be pos int"
        assert isinstance(page_size, int) and page_size > 0, "page_size ("")"

        """Find start and end indices using prev function (index_range)"""
        start_index, end_index = index_range(page, page_size)

        """Retrieves the dataset"""
        dataset = self.dataset()

        """Return correct page of dataset based on start and end"""
        return dataset[start_index:end_index]
