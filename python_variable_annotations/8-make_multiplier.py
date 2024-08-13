#!/usr/bin/env python3
"""Returns a float multiplied"""
from typing import Callable


def make_mutliplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_funtion(value: float) -> float:
        return value * multiplier
    return multiplier_funtion
