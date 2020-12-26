""" AOC Day 23 """
from pathlib import Path
from typing import List, Union


def first(filename: Union[str, Path], num_rounds: int = 100) -> int:
    """
    Part 1
    """
    with open(filename, "rt") as infile:
        cups = [int(x) for x in infile.read().strip()]

    for num_round in range(num_rounds):
        cur_idx = 0
        cur_idx = num_round % len(cups)
        cur_cup = cups[cur_idx]

        removed_cups = [cups[(cur_idx + i) % len(cups)] for i in range(1, 4)]

        next_cup = ((cur_cup - 1) + len(cups)) % len(cups)
        if next_cup == 0:
            next_cup = len(cups)

        while next_cup in removed_cups:
            next_cup -= 1
            if next_cup == 0:
                next_cup = len(cups)

        next_cups: List[int] = []
        while len(next_cups) < len(cups):
            this_cup = cups[cur_idx]
            if this_cup in removed_cups:
                pass
            elif this_cup == next_cup:
                next_cups.append(next_cup)
                next_cups.extend(removed_cups)
            else:
                next_cups.append(this_cup)

            cur_idx = (cur_idx + 1) % len(cups)

        cups = (
            next_cups[-(num_round % len(cups)) :]
            + next_cups[: -(num_round % len(cups))]
        )

    idx = cups.index(1)
    output = []
    cur_idx = (idx + 1) % len(cups)
    while cur_idx != idx:
        output.append(cups[cur_idx])
        cur_idx += 1
        cur_idx %= len(cups)

    return int("".join(map(str, output)))


def second(filename: Union[str, Path], num_rounds: int = 10_000_000) -> int:
    """
    Part 2
    """
    vals: List[int] = []
    with open(filename, "rt") as infile:
        for cup in infile.read().strip():
            vals.append(int(cup) - 1)

    vals.extend(range(max(vals) + 1, 1_000_000))

    num_vals = 1_000_000
    val_to_next = [0] * num_vals
    for val, next_val in zip(vals[:-1], vals[1:]):
        val_to_next[val] = next_val
    val_to_next[vals[-1]] = vals[0]

    cur_val = vals[0]

    for _ in range(num_rounds):
        removed_vals = [
            val_to_next[cur_val],
            val_to_next[val_to_next[cur_val]],
            val_to_next[val_to_next[val_to_next[cur_val]]],
        ]

        next_cup = (cur_val - 1) % num_vals
        while next_cup in removed_vals:
            next_cup = (next_cup - 1) % num_vals

        val_to_next[cur_val] = val_to_next[removed_vals[-1]]
        new_next = val_to_next[next_cup]
        val_to_next[next_cup] = removed_vals[0]
        val_to_next[removed_vals[-1]] = new_next

        cur_val = val_to_next[cur_val]

    return (val_to_next[0] + 1) * (val_to_next[val_to_next[0]] + 1)
