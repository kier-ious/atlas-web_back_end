#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list for
    those particular pagination parameters."""
    # Caluclate the start of the index of current page
    start_index = (page - 1) * page_size
    # Caluclate the end " "
    end_index = start_index + page_size

    return start_index, end_index
