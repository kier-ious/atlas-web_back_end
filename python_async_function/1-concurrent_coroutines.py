#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay value

    Returns:
        list[float]: List of delays (float values) in ascending order
    """

    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)
    return delays
