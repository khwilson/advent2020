""" AOC Day 10 """
from collections import Counter, defaultdict
from pathlib import Path
from typing import Union


def first(filename: Union[str, Path]) -> int:
    """
    Sort the input, prepend with 0 and append with 3 + the max.

    Return:
        (# of successive differences == 1) * (# of successive differences == 3)
    """
    with open(filename, "rt") as infile:
        jolts = sorted(int(line.strip()) for line in infile)

    jolts = [0] + jolts + [jolts[-1] + 3]

    diffs = Counter(right - left for left, right in zip(jolts[:-1], jolts[1:]))
    return diffs[3] * diffs[1]


def second(filename: Union[str, Path]) -> int:
    """
    Return the number of subsequences of the sorted input with the following properties:
        * The last entry is always the last entry of the sorted input
        * The first entry is 1, 2, or 3
        * There is never a successive difference that is > 3

    Strategy: Dynamic programming!
    """
    with open(filename, "rt") as infile:
        jolts = sorted(int(line.strip()) for line in infile)

    num_valid_sequences_with_min = defaultdict(int)

    num_valid_sequences_with_min[jolts[-1]] = 1
    for jolt in reversed(jolts[:-1]):
        num_valid_sequences_with_min[jolt] = (
            num_valid_sequences_with_min[jolt + 1]
            + num_valid_sequences_with_min[jolt + 2]
            + num_valid_sequences_with_min[jolt + 3]
        )

    return (
        num_valid_sequences_with_min[1]
        + num_valid_sequences_with_min[2]
        + num_valid_sequences_with_min[3]
    )
