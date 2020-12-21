""" AOC Day 8 """
import itertools as its
import math
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple, Union

import numpy as np

MONSTER = """\
                  # |
#    ##    ##    ###|
 #  #  #  #  #  #   |
"""


def get_rotations(tile: np.ndarray) -> List[np.ndarray]:
    """
    Compute all the 8 SO2(Z) actions on tile
    """
    rotations = [tile.copy()]
    for i in range(1, 8):
        if i % 2 == 0:
            tile = tile[::-1, :]
        else:
            tile = tile.T
        rotations.append(tile.copy())
    return rotations


def dfs_the_sea(
    size: int,
    adj_list: Dict[int, Dict[int, Dict[str, List[Tuple[int, int]]]]],
    final_tile_ids: List[int],
) -> bool:
    """
    Do a depth first search through all possible layouts given the
    available paths enumerated by adj_list. If we hit a full size * size grid,
    return True up the chain. Else return False.

    Note that we operate directly on final_tile_ids. If you get back an array
    of the same length you put in, then we returned False. Else, expect a size * size
    array reading left-right-top-bottom
    """
    if len(final_tile_ids) == size * size:
        return True

    pos = len(final_tile_ids)

    needs_to_match = []
    if pos - size >= 0:
        needs_to_match.append(final_tile_ids[pos - size] + ("down",))
    if ((pos - 1) % size) < (pos % size):
        needs_to_match.append(final_tile_ids[pos - 1] + ("right",))

    could_be = {
        (tile_id, rotation)
        for tile_id, rotations in adj_list.items()
        for rotation in rotations
    }
    for tile_id, rotation, dir in needs_to_match:
        could_be &= adj_list[tile_id][rotation][dir]

    for tile_id, rotation in could_be:
        final_tile_ids.append((tile_id, rotation))
        if dfs_the_sea(size, adj_list, final_tile_ids):
            return True
        final_tile_ids.pop()

    return False


def do_part_one(filename: Union[str, Path]) -> int:
    """
    Find the appropriate sea layout
    """
    with open(filename, "rt") as infile:
        raw_tiles = infile.read().split("\n\n")

    tiles_with_rotations = {}
    for raw_tile in raw_tiles:

        stile = raw_tile.split("\n")
        header = stile[0]
        main = stile[1:]

        tile_id = int(re.findall(r"\d+", header)[0])
        tile = np.array([[val == "#" for val in row] for row in main], dtype=bool)

        tiles_with_rotations[tile_id] = get_rotations(tile)

    size = int(math.sqrt(len(tiles_with_rotations)))

    # Next setup all possible ways to do the adjacencies
    # tile_id -> rotation -> lrud -> List[tile_id]
    adj_list = defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
    for tile_id, rotations in tiles_with_rotations.items():
        for rotation, tile in enumerate(rotations):
            for other_tile_id, other_rotations in tiles_with_rotations.items():
                if tile_id == other_tile_id:
                    continue

                adj = adj_list[tile_id][rotation]
                for other_rotation, other_tile in enumerate(other_rotations):
                    if (tile[0, :] == other_tile[-1, :]).all():
                        adj["up"].add((other_tile_id, other_rotation))
                    if (tile[-1, :] == other_tile[0, :]).all():
                        adj["down"].add((other_tile_id, other_rotation))
                    if (tile[:, 0] == other_tile[:, -1]).all():
                        adj["left"].add((other_tile_id, other_rotation))
                    if (tile[:, -1] == other_tile[:, 0]).all():
                        adj["right"].add((other_tile_id, other_rotation))

    final_tile_ids = []
    dfs_the_sea(size, adj_list, final_tile_ids)

    return tiles_with_rotations, final_tile_ids, size


def first(filename) -> int:
    """ Part 1 """
    _, final_tile_ids, size = do_part_one(filename)
    return math.prod(final_tile_ids[idx][0] for idx in [0, size - 1, -1, -size])


def second(filename: Union[str, Path]) -> int:
    """
    Part 2
    """
    tiles_with_rotations, final_tile_ids, size = do_part_one(filename)

    # Trim the edges of the squares
    rows = []
    for row_num in range(size):
        this_row = []
        for col_num in range(size):
            tile_id, rotation = final_tile_ids[row_num * size + col_num]
            this_row.append(tiles_with_rotations[tile_id][rotation][1:-1, 1:-1])
        rows.append(np.hstack(this_row))
    the_sea = np.vstack(rows)

    # Make the monster
    monster = np.vstack(
        [[x == "#" for x in row] for row in MONSTER.replace("|", "").split("\n") if row]
    )

    # Keep track of the found squares
    is_found = np.zeros_like(the_sea, dtype=bool)

    # Go on a hunt (note we may need to rotate the sea / monster)
    num_monster = monster.sum()
    for monster in get_rotations(monster):
        width, height = monster.shape
        for i, j in its.product(*map(range, the_sea.shape)):
            if i + width >= the_sea.shape[0] or j + height >= the_sea.shape[1]:
                continue

            if (monster & the_sea[i : i + width, j : j + height]).sum() == num_monster:
                is_found[i : i + width, j : j + height] |= monster

        # The prompt said there's only one correct rotation
        if is_found.any():
            return the_sea.sum() - is_found.sum()
