#!/usr/bin/env python3
"""The comprehension of async"""
import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel

    Returns:
        float: Total runtime returned in seconds
    """
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    end_time = time.time()
    total_runtime = end_time - start_time

    return total_runtime
