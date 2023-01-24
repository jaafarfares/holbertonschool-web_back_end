#!/usr/bin/env python3
"""_summary_
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio



def task_wait_random(max_delay):
    """_summary_
    asyncio.Task implementation
    """
    return asyncio.create_task(wait_random())
