#!/usr/bin/env python3
"""Returns the sum of the list of mixed types"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of the list"""
    return sum(mxd_lst)
