""" AOC Day 11 """
import itertools as its
from pathlib import Path
from typing import Iterator, List, Optional, Tuple, Union

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"

AROUND = tuple([(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == j == 0)])


def step_in_direction(
    i: int,
    j: int,
    max_i: int,
    max_j: int,
    dir_i: int,
    dir_j: int,
    max_steps: Optional[int] = None,
) -> Iterator[Tuple[int, int]]:
    num_steps = (max_steps and range(max_steps)) or its.count()
    for _ in num_steps:
        i += dir_i
        j += dir_j
        if not ((0 <= i < max_i) and (0 <= j < max_j)):
            return
        yield i, j


def detect(
    layout: List[str], i: int, j: int, max_steps: Optional[int] = None
) -> Iterator[str]:
    """
    Yield the collection of tiles that can be seen on the board (layout)
    from position (i, j) within max_steps. See `game_of_life` for what
    it means to be able to be seen.
    """
    num_rows, num_cols = len(layout), len(layout[0])
    for di, dj in AROUND:
        for vi, vj in step_in_direction(i, j, num_rows, num_cols, di, dj, max_steps):
            if layout[vi][vj] != FLOOR:
                yield layout[vi][vj]
                break
            yield FLOOR


def game_of_life(
    layout: List[str], cutoff: int, max_steps: Optional[int] = None
) -> List[str]:
    """
    Iterate the game board (layout) according to these rules:
        * For each tile, the collection of tiles that can be seen from that tile
          is the first non-floor tile in each of the 8 directions from that tile.
        * If max_steps is not None, then a tile can only be seen if it is within
          max_steps of the tile in each direction.
        * If a tile is EMPTY, it becomes OCCUPIED if all the tiles that can be
          seen from it are either EMPTY or FLOOR
        * If a tile is OCCUPIED, it becomes EMPTY if at least `cutoff` of the
          tiles that can be seen from it are OCCUPIED.

    Stop iterating when the board stabilizes. Return that stable board.
    """
    while True:
        new_layout = []
        for i, row in enumerate(layout):
            new_row = []
            for j, col in enumerate(row):
                if col == EMPTY:
                    all_empty = all(
                        tile != OCCUPIED for tile in detect(layout, i, j, max_steps)
                    )
                    if all_empty:
                        new_row.append(OCCUPIED)
                    else:
                        new_row.append(EMPTY)
                elif col == OCCUPIED:
                    total_occupied = sum(
                        tile == OCCUPIED for tile in detect(layout, i, j, max_steps)
                    )
                    if total_occupied >= cutoff:
                        new_row.append(EMPTY)
                    else:
                        new_row.append(OCCUPIED)
                else:
                    new_row.append(FLOOR)
            new_layout.append("".join(new_row))

        if "".join(new_layout) == "".join(layout):
            break

        layout = new_layout

    return layout


def first(filename: Union[str, Path]) -> int:
    """
    Iterate the Game of Life board according to the first set of
    rules until it stabilizes. Return the total number of occupied
    seats upon stabilization.
    """
    with open(filename, "rt") as infile:
        layout = [line.strip() for line in infile]

    return sum(
        col == OCCUPIED for row in game_of_life(layout, 4, max_steps=1) for col in row
    )


def second(filename: Union[str, Path]) -> int:
    """
    Iterate the Game of Life board according to the second set of
    rules until it stabilizes. Return the total number of occupied seats
    upon stabilization.
    """
    with open(filename, "rt") as infile:
        layout = [line.strip() for line in infile]

    return sum(col == OCCUPIED for row in game_of_life(layout, 5) for col in row)
