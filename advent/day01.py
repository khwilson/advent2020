""" AOC Day 1 """
import itertools as its
from pathlib import Path
from typing import Union

import numpy as np


def first(filename: Union[str, Path]) -> int:
    """
    Find the pair of integers listed that sum to 2020 and return their product

    Args:
        filename: The location of the input

    Returns:
        The product of the pair of integers that sum to 2020
    """
    seen = np.zeros(2021, dtype=bool)
    with open(filename, "rt") as infile:
        for line in infile:
            val = int(line.strip())
            if 0 <= val <= 2020:
                if seen[2020 - val]:
                    return val * (2020 - val)
                seen[val] = True
    raise ValueError("Something went wrong")


def second(filename: str) -> int:
    """
    Find the product of the _three_ listed integers that sum to 2020.

    Args:
        filename: The location of the input, which is one integer per line

    Returns:
        The product of the three integers that sum to 2020
    """
    with open(filename, "rt") as infile:
        values = {
            val
            for line in infile
            if line.strip() and 0 <= (val := int(line.strip())) <= 2020
        }

    # Quadratic method: Just compute all sums of pairs and find overlapping values
    for left, right in its.combinations(values, 2):
        if 2020 - left - right in values:
            return left * right * (2020 - left - right)

    raise ValueError("Something went wrong in part 2")
