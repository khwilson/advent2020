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


def read_board(filename: Union[str, Path], dim: int = 3) -> SpaceType:
    """
    Read in the board from a file (which contains a 2d board). The
    coordinates will be right 0-padded until they are `dim` wide
    """
    space: SpaceType = defaultdict(bool)
    with open(filename, "rt") as infile:
        for y, line in enumerate(infile):
            line = line.strip()
            for x, char in enumerate(line):
                coord = tuple([x, y] + [0] * (dim - 2))
                if char == ACTIVE:
                    space[coord] = True
                elif char == INACTIVE:
                    pass
                    # space[coord] = False
                else:
                    raise ValueError(f"Invalid character: {char}")
    return space


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
                if 2 <= sum(space[key] for key in neighbors(*key)) <= 3:
                    new_space[key] = True
            else:
                if sum(space[key] for key in neighbors(*key)) == 3:
                    new_space[key] = True
        space = new_space
    return space


def first(filename: Union[str, Path]) -> int:
    """
    Play a 3 dimensional game of life according to the rules in `play_game`
    """
    # (x, y, z) -> is_active
    space: Dict[Tuple[int, int, int], bool] = read_board(filename)

    space = play_game(space, 6)
    return sum(space.values())


def second(filename: Union[str, Path]) -> int:
    """
    Play a 4-dimensional game of life according to the rules in `play_game`.

    NOTE: This is probably super inefficient with a lot of extra checks and
          additional square being activated. However, it's AOC, so :-D
    """
    # (x, y, z, w) -> is_active
    space: Dict[Tuple[int, int, int, int], bool] = read_board(filename, dim=4)

    space = play_game(space, 6)
    return sum(space.values())
