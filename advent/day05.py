""" AOC Day 5 """
from pathlib import Path
from typing import Union


def convert_all(string: str) -> int:
    """
    Input is the binary representation of a number. R or B means 1. L or F means 0.
    Return the value of this binary representation
    """
    return int("".join("1" if char in ("R", "B") else "0" for char in string), 2)


def first(filename: Union[str, Path]) -> int:
    """
    Return the maximum seat id among my inputs
    """
    with open(filename, "rt") as infile:
        return max(convert_all(line.strip()) for line in infile)


def second(filename: Union[str, Path]) -> int:
    """
    There should be exactly one pair of numbers that are exactly two apart.
    Return their median (aka, my seat)
    """
    with open(filename, "rt") as infile:
        seen_seats = sorted(convert_all(line.strip()) for line in infile)

    for left, right in zip(seen_seats, seen_seats[1:]):
        if right - left == 2:
            return right - 1
    raise ValueError("Something went wrong")
