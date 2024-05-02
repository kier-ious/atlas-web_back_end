#!/usr/bin/env python3
"""The basics of async"""
import time
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create an asyncio.Task for the wait_random coroutine

    Args:
        max_delay (int): Max delay value

    Returns:
        asyncio.Task: Task that will execute wait_random
    """
    return asyncio.create_task(wait_random(max_delay))
