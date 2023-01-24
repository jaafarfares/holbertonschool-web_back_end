#!/usr/bin/env python3
"""_summary_
"""
from typing import List
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """_summary_
    return the list of all the delays
    """
    delays = []
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
        delays = sorted(delays)
    return delays
