#!/usr/bin/env python3
"""Async Comprehensions"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Frankly, my dear, I don't give a damn"""
    return [i async for i in async_generator()]
