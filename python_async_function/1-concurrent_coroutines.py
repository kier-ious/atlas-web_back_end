#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times with the specified max_delay

    Args:
        n (int): Number of times to spawn wait_random
        max_delay (int): Maximum delay value

    Returns:
        list[float]: List of delays (float values) in ascending order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return results
