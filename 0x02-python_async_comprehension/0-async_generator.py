#!/usr/bin/env python3
"""    # loop 10 times
    for i in range(10):
        # wait 1 second asynchronously
        await asyncio.sleep(1)
        # yield a random number between 0 and 10
"""
import random
import asyncio
from typing import List, Generator


async def async_generator() -> Generator[float, float, float]:
    """
    use the async for loop to iterate over
    the values yielded by the coroutine
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
