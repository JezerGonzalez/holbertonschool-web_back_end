#!/usr/bin/env python3
"""Returns the sum of the list of mixed types"""
from typing import List


def sum_mixed_list(mxd_list: List[float, int]) -> float:
    """returns the sum of the list"""
    return sum(mxd_list)
