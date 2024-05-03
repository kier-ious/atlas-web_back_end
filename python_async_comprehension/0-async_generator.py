#!/usr/bin/env python3
"""The comprehension of async"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]: # type: ignore
    """Async generator that yields 10 random #'s between 0-10

    Yields:
        float: Random floating number between 0-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
