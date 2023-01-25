#!/usr/bin/env python3
"""_summary_
"""

import random
import asyncio




async def async_generator():
    for i in range(4):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
