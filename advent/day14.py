""" AOC Day 14 """
import itertools as its
import re
from pathlib import Path
from typing import Any, Iterator, List, Union

import numpy as np


def str_to_array(val: str) -> np.ndarray:
    """
    Convert a decimal integer as a string to a 36-wide bit
    array representing its binary expansion (high bit = index 0)
    """
    val = np.array([char == "1" for char in bin(int(val))[2:]])
    return np.hstack([np.zeros(36 - len(val), dtype=bool), val])


def array_to_int(arr: np.ndarray) -> int:
    """
    Convert a bit array to its integer equivalent (high bit = index 0)
    """
    return int("".join("1" if val else "0" for val in arr), 2)


def powerset(vals: List[Any]) -> Iterator[Any]:
    """
    For any given list of things, yield all elements of its powerset
    """
    yield from its.chain.from_iterable(
        its.combinations(vals, i) for i in range(len(vals) + 1)
    )


def first(filename: Union[str, Path]) -> int:
    """
    Part 1
    """
    ones_mask = np.zeros(36, dtype=bool)
    zeros_mask = np.ones(36, dtype=bool)
    memory = {}
    with open(filename, "rt") as infile:
        for line in infile:
            if line.startswith("mask"):
                mask = line.strip().split(" ")[-1]
                ones_mask = np.array([x == "1" for x in mask])
                zeros_mask = np.array([x != "0" for x in mask])
            elif line.startswith("mem"):
                register = re.findall(r"mem\[(\d+)\]", line)[0]
                val = str_to_array(line.strip().split(" ")[-1])
                memory[register] = (val | ones_mask) & zeros_mask
            else:
                raise ValueError("Something went wrong")

    return sum(map(array_to_int, memory.values()))


def second(filename: Union[str, Path]) -> int:
    """
    Part 2
    """
    ones_mask = np.zeros(36, dtype=bool)
    floating_mask = np.zeros(36, dtype=bool)
    memory = {}
    with open(filename, "rt") as infile:
        for line in infile:
            if line.startswith("mask"):
                mask = line.strip().split(" ")[-1]
                ones_mask = np.array([x == "1" for x in mask])
                floating_mask = np.array([x == "X" for x in mask])

            elif line.startswith("mem"):
                register = str_to_array(re.findall(r"mem\[(\d+)\]", line)[0])
                register = (register | ones_mask) & ~floating_mask

                val = int(line.strip().split(" ")[-1])

                for combo in powerset(np.where(floating_mask)[0]):
                    zeros_mask = np.zeros_like(ones_mask)
                    zeros_mask[list(combo)] = True
                    memory[array_to_int(register | zeros_mask)] = val
            else:
                raise ValueError("Something went wrong")

    return sum(memory.values())
