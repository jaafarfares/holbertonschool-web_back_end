#!/usr/bin/env python3
"""
_summary_
"""
import random
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_
    Async Comprehensions
    Returns:
        list[float]: random numbers
    """
    numbers = []
    async for i in async_generator():
        numbers.append(i)
    return numbers
