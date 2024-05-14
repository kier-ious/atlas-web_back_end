#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dict w/ pagination infor bases on indexies"""

        indexed_dataset = self.indexed_dataset()
        num_items = len(indexed_dataset)

        """Ensure index is w/in set valid range"""
        if index is not None:
            assert index < num_items, (
                f"index {index} is out of range(total items: {num_items})"
            )

        """Find next index to query w/"""
        next_index = min(
            index + page_size, num_items) if index is not None else page_size

        """Retrieve data from the current page"""
        data = [indexed_dataset[i] for i in range(index, next_index)]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
