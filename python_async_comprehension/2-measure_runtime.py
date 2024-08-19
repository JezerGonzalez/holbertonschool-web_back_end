#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Tu mai por si acaso"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension())
    end_time = time.perf_counter()
    total = end_time - start_time
    return total
