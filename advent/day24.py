""" AOC Day 8 """
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple, Union

WHITE = 0
BLACK = 1


def get_board(filename: Union[str, Path]) -> Dict[Tuple[int, int, int], int]:
    """
    Parse the incoming file for the starting state of the hexagonal Life board
    """
    tiles: Dict[int] = defaultdict(lambda: WHITE)
    with open(filename, "rt") as infile:
        for line in infile:
            a, r, c = 0, 0, 0
            line = line.strip()
            idx = 0
            while idx < len(line):
                direction = line[idx]
                if direction == "n":
                    direction = direction + line[idx + 1]
                    if direction == "nw":
                        a, r, c = 1 - a, r - (1 - a), c - (1 - a)
                    elif direction == "ne":
                        a, r, c = 1 - a, r - (1 - a), c + a
                    else:
                        raise ValueError
                    idx += 2
                elif direction == "s":
                    direction = direction + line[idx + 1]
                    if direction == "sw":
                        a, r, c = 1 - a, r + a, c - (1 - a)
                    elif direction == "se":
                        a, r, c = 1 - a, r + a, c + a
                    else:
                        raise ValueError
                    idx += 2
                elif direction == "e":
                    a, r, c = a, r, c + 1
                    idx += 1
                elif direction == "w":
                    a, r, c = a, r, c - 1
                    idx += 1
                else:
                    raise ValueError(f"Bad direction: {direction}")
            tiles[(a, r, c)] = WHITE if tiles[(a, r, c)] == BLACK else BLACK
    return tiles


def neighbors(a: int, r: int, c: int) -> List[Tuple[int, int, int]]:
    """
    Return the list of all six neighbors of the passed coordinate
    """
    return [
        (1 - a, r - (1 - a), c - (1 - a)),  # NW
        (1 - a, r - (1 - a), c + a),  # NE
        (a, r, c + 1),  # E
        (1 - a, r + a, c + a),  # SE
        (1 - a, r + a, c - (1 - a)),  # SW
        (a, r, c - 1),  # W
    ]


def first(filename: Union[str, Path]) -> int:
    """
    How many black square are there on the board?
    """
    return sum(get_board(filename).values())


def second(filename: Union[str, Path]) -> int:
    """
    Play a game of life for 100 rounds. After which, how many black
    squares are on the board?
    """
    board = get_board(filename)

    for _ in range(100):
        new_board = defaultdict(lambda: WHITE)
        to_visit = {key for key, val in board.items() if val == BLACK}
        to_visit = to_visit | {
            neighbor for tile in to_visit for neighbor in neighbors(*tile)
        }
        for tile in to_visit:
            count_black_neighbors = sum(
                board[neighbor] == BLACK for neighbor in neighbors(*tile)
            )
            if board[tile] == WHITE:
                if count_black_neighbors == 2:
                    new_board[tile] = BLACK
            else:
                if count_black_neighbors in (1, 2):
                    new_board[tile] = BLACK
        board = new_board

    return sum(board.values())
