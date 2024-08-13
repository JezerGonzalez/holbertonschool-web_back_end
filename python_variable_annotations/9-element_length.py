#!/usr/bin/env python3
"""Fix my code type shii"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Some more documentation"""
    return [(i, len(i)) for i in lst]
