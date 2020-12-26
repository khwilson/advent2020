""" AOC Day 8 """
import itertools as its
from pathlib import Path
from typing import Union

import numpy as np


def disrete_logarithm(answer, base, mod):
    """
    Compute x where answer == pow(base, x, mod). Some notes:
        * This is done by linearly searching, so don't actually use this
          for real cryptographic applications
        * This probably won't do what you think it does if base isn't a
          primitive root modulo mod
    """
    log = 1
    val = base
    while True:
        if answer == val:
            return log
        log += 1
        val = (val * base) % mod


def first(filename: Union[str, Path]) -> int:
    """
    Our inputs are 7^x and 7^y modulo 20201227. With these inputs,
    compute 7^{xy}.
    """
    subject_number = 7
    card_public_key, door_public_key = map(
        int, open(filename, "rt").read().strip().split()
    )
    card_loop_size = disrete_logarithm(card_public_key, subject_number, 20201227)
    return pow(door_public_key, card_loop_size, 20201227)


def second(filename: Union[str, Path]) -> str:
    """
    Part 2
    """
    return "Merry Christmas!"
