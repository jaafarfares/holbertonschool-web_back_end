#!/usr/bin/env python3
"""_summary_
"""
import random
import asyncio
from typing import List, Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    numbers = []
    async for i in async_generator():
        numbers.append(i)
    return numbers




