""" AOC Day 8 """
import itertools as its
from pathlib import Path
from typing import Optional, Union


def first(filename: Union[str, Path], preamble_length: int = 25) -> Optional[int]:
    """
    Return the first number that cannot be written as the sum of two numbers
    among the previous `preamble_length` numbers

    If no such set of numbers is found, return None.
    """
    with open(filename, "rt") as infile:
        data = [int(line.strip()) for line in infile]

    for i, num in enumerate(data[preamble_length:], preamble_length):
        for left, right in its.combinations(data[i - preamble_length : i], 2):
            if num == left + right:
                break
        else:
            return num

    return None


def second(filename: Union[str, Path], preamble_length: int = 25) -> Optional[int]:
    """
    Find the first contiguous set of numbers that sum to the return value of
    `first`. Then return the sum of the minimum and maximum of these numbers.

    If no such set of numbers is found, return None.
    """
    num = first(filename, preamble_length=preamble_length)
    with open(filename, "rt") as infile:
        data = [int(line.strip()) for line in infile]

    for left in range(len(data)):
        total = 0
        for right, val in enumerate(data[left:], left):
            total += val
            if total == num:
                return min(data[left : right + 1]) + max(data[left : right + 1])

    return None
