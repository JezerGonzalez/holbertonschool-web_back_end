#!/usr/bin/env python3
"""Fix my code type shii"""
from typing import List, Union, Tuple


def element_length(lst: List[Union[int, float]]) -> Tuple[int, tuple] :
    return [(i, len(i)) for i in lst]
