#!/usr/bin/env python3
"""Async Generator"""
import asyncio
import random


async def asyn_generator ():
    """Give me liberty, give me death"""
    for number in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
