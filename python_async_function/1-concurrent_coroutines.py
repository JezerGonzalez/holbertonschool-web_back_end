#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """It can wait a bit"""
    delays = []
    for _ in range(n):
        result = await wait_random(max_delay)
        delays.append(result)
    sorted(delays)
    return delays
