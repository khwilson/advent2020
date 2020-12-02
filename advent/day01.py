""" AOC Day 1 """
import itertools as its
from collections import Counter
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
        values_with_counts = Counter(
            val
            for line in infile
            if (sline := line.strip()) and 0 <= (val := int(sline)) <= 2020
        )

    values = set(values_with_counts)

    # Quadratic method: Just compute all sums of pairs and find overlapping values
    for left, right in its.combinations(values, 2):
        val = 2020 - left - right
        if val in values:
            # Make sure that these lines are distinct!
            if val == left:
                if val == right:
                    # Shouldn't happen because gcd(2020, 3) = 1, but for completeness
                    if values_with_counts[val] <= 2:
                        continue
                else:
                    if values_with_counts[val] <= 1:
                        continue
            elif val == right:
                if values_with_counts[val] <= 1:
                    continue
                # Do a linear pass to make sure that there are
            return left * right * val

    raise ValueError("Something went wrong in part 2")
