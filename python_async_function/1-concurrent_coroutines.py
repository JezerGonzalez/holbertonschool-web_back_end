#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """It awaits"""
    delays = []

    for x in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    for i in range(1, len(delays)):
        key = delays[i]
        j = i - 1
        while j >= 0 and key < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1] = key

    return delays
