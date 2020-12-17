""" AOC Day 17 """
import itertools as its
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterator, Tuple, Union

import numpy as np

ACTIVE = "#"
INACTIVE = "."


SpaceType = Dict[Tuple[int, ...], bool]


def neighbors(*args: Tuple[int, ...]) -> Iterator[Tuple[int, ...]]:
    """
    Yield each of the points in space whose coordinates are at most
    one off from the passed coordinate. Excludes the point itself
    """
    for incs in its.product([-1, 0, 1], repeat=len(args)):
        if not all(i == 0 for i in incs):
            yield tuple([x + i for x, i in zip(args, incs)])


def play_game(space: SpaceType, num_rounds: int) -> SpaceType:
    """
    Play a game of life according to the following rules:
        * If a square is active and exactly 2 or 3 of its neighbors are also active,
          the square remains active. Otherwise, the square becomes inactive.
        * If a square is inactive but exactly 3 of its neighbors are active,
          the square becomes active. Otherwise, the square remains inactive.
    """
    for _ in range(num_rounds):
        # Make sure to look at least one outside of the currently active cubes
        keys = {neighbor for key in space for neighbor in neighbors(*key)} | set(space)

        new_space = defaultdict(bool)
        for key in keys:
            if space[key]:
                new_space[key] = 2 <= sum(space[key] for key in neighbors(*key)) <= 3
            else:
                new_space[key] = sum(space[key] for key in neighbors(*key)) == 3
        space = new_space
    return space


def first(filename: Union[str, Path]) -> int:
    """
    Play a 3 dimensional game of life according to the rules in `play_game`
    """
    # (x, y, z) -> is_active
    space: Dict[Tuple[int, int, int], bool] = defaultdict(bool)

    with open(filename, "rt") as infile:
        for y, line in enumerate(infile):
            line = line.strip()
            for x, char in enumerate(line):
                if char == ACTIVE:
                    space[(x, y, 0)] = True
                elif char == INACTIVE:
                    space[(x, y, 0)] = False
                else:
                    raise ValueError(f"Invalid character: {char}")

    space = play_game(space, 6)
    return sum(space.values())


def second(filename: Union[str, Path]) -> int:
    """
    Play a 4-dimensional game of life according to the rules in `play_game`.

    NOTE: This is probably super inefficient with a lot of extra checks and
          additional square being activated. However, it's AOC, so :-D
    """
    # (x, y, z, w) -> is_active
    space: Dict[Tuple[int, int, int, int], bool] = defaultdict(bool)

    with open(filename, "rt") as infile:
        for y, line in enumerate(infile):
            line = line.strip()
            for x, char in enumerate(line):
                if char == ACTIVE:
                    space[(x, y, 0, 0)] = True
                elif char == INACTIVE:
                    space[(x, y, 0, 0)] = False
                else:
                    raise ValueError(f"Invalid character: {char}")

    space = play_game(space, 6)
    return sum(space.values())
