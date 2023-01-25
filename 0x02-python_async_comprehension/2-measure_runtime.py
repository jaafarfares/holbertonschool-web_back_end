#!/usr/bin/env python3
"""_summary_
"""
import time
from typing import List
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> List[float]:
    """
    Run time for four parallel comprehensions
    Returns:
        _type_: _description_
    """
    start = time.time()
    for i in range(4):
        await asyncio.gather((async_comprehension()))
        end = time.time()
        total = start - end
    return total
