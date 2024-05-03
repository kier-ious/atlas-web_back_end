#!/usr/bin/env python3
"""The comprehension of async"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async coroutine that collects 10 random #'s using current func

    Returns:
        List[float]: List containing the 10 random floating #'s
    """
    random_number = [
        random_number async for random_number in async_generator()
    ]

    return random_number
