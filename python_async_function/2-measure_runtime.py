#!/usr/bin/env python3
"""The basics of async"""
import time
import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time per iteration of wait_n

    Args:
        n (int): Number of times to excute wait_n
        max_delay (int): Max delay value for wait_n

    Returns:
        float: Average execution time per iteration of wait_n
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time
    average_time = total_time / n

    return average_time
