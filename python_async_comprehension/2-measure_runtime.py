#!/usr/bin/env python3
"""The comprehension of async"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel

    Returns:
        float: Total runtime returned in seconds
    """
    start_time = asyncio.get_event_loop().time()

    # Execute prev mod 4 times in parallel using asyncio.gather
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
