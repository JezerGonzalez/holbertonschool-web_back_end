#!/usr/bin/env python3
"""Returns a float multiplied"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Yes"""
    def multiplier_funtion(value: float) -> float:
        """Absolutely"""
        return value * multiplier
    return multiplier_funtion
