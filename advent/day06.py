""" AOC Day 6 """
import re
from collections import Counter
from pathlib import Path
from typing import Union


def first(filename: Union[str, Path]) -> int:
    """
    In each group of letters (separated by a double newline), return
    the number of distinct letters.
    """
    with open(filename, "rt") as infile:
        groups = infile.read().strip().split("\n\n")

    return sum(len(set(re.sub(r"\s", "", group))) for group in groups)


def second(filename: Union[str, Path]) -> int:
    """
    For each group of letters (separated by a double newline), count the
    number of letters that appear on all the lines in the group. Then
    return the total number of such letters. (Letters do not need to
    be distinct _between_ groups, only within groups.)
    """
    with open(filename, "rt") as infile:
        groups = infile.read().strip().split("\n\n")

    groups = [group.split("\n") for group in groups]

    return sum(
        sum(val == len(group) for val in Counter("".join(group)).values())
        for group in groups
    )
