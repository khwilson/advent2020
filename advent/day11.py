""" AOC Day 11 """
from pathlib import Path
from typing import List, Tuple, Union


FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"

AROUND = tuple([(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == j == 0)])


def adj_ij(i: int, j: int, max_i: int, max_j: int) -> List[Tuple[int, int]]:
    valid_is = [vi for vi in [i - 1, i, i + 1] if 0 <= vi < max_i]
    valid_js = [vi for vi in [j - 1, j, j + 1] if 0 <= vi < max_j]

    out = [(vi, vj) for vi in valid_is for vj in valid_js if not (vi == i and vj == j)]
    return out


def step_in_direction(i: int, j: int, max_i: int, max_j: int, dir_i: int, dir_j: int):
    while True:
        i += dir_i
        j += dir_j
        if not ((0 <= i < max_i) and (0 <= j < max_j)):
            return
        yield i, j


def detect(layout: List[str], i: int, j: int, dir_i: int, dir_j: int) -> str:
    for vi, vj in step_in_direction(i, j, len(layout), len(layout[0]), dir_i, dir_j):
        if layout[vi][vj] in [EMPTY, OCCUPIED]:
            return layout[vi][vj]
    return FLOOR


def first(filename: Union[str, Path]) -> int:
    """
    Part 1
    """
    with open(filename, "rt") as infile:
        layout = [line.strip() for line in infile]

    while True:
        new_layout = []
        for i, row in enumerate(layout):
            new_row = []
            for j, col in enumerate(row):
                if col == EMPTY:
                    if all(
                        layout[vi][vj] != OCCUPIED
                        for vi, vj in adj_ij(i, j, len(layout), len(row))
                    ):
                        new_row.append(OCCUPIED)
                    else:
                        new_row.append(EMPTY)
                elif col == OCCUPIED:
                    if (
                        sum(
                            layout[vi][vj] == OCCUPIED
                            for vi, vj in adj_ij(i, j, len(layout), len(row))
                        )
                        >= 4
                    ):
                        new_row.append(EMPTY)
                    else:
                        new_row.append(OCCUPIED)
                else:
                    new_row.append(FLOOR)
            new_layout.append("".join(new_row))

        if "".join(new_layout) == "".join(layout):
            break

        layout = new_layout

    return sum(col == OCCUPIED for row in layout for col in row)


def second(filename: Union[str, Path]) -> int:
    """
    Part 2
    """
    with open(filename, "rt") as infile:
        layout = [line.strip() for line in infile]

    while True:
        new_layout = []
        for i, row in enumerate(layout):
            new_row = []
            for j, col in enumerate(row):
                if col == EMPTY:
                    if all(
                        detect(layout, i, j, dir_i, dir_j) != OCCUPIED
                        for dir_i, dir_j in AROUND
                    ):
                        new_row.append(OCCUPIED)
                    else:
                        new_row.append(EMPTY)

                elif col == OCCUPIED:
                    if (
                        sum(
                            detect(layout, i, j, dir_i, dir_j) == OCCUPIED
                            for dir_i, dir_j in AROUND
                        )
                        < 5
                    ):
                        new_row.append(OCCUPIED)
                    else:
                        new_row.append(EMPTY)
                else:
                    new_row.append(FLOOR)
            new_layout.append("".join(new_row))

        if "".join(new_layout) == "".join(layout):
            break

        layout = new_layout

    return sum(col == OCCUPIED for row in layout for col in row)
