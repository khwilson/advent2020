""" AOC Day 15 """
from pathlib import Path
from typing import Union


def play_game(filename: Union[str, Path], num_rounds: int) -> int:
    """ See instructions on `first` """
    last_spoken = {}
    with open(filename, "rt") as infile:
        data = [int(x) for x in infile.read().strip().split(",")]

    for i, datum in enumerate(data[:-1], 1):
        last_spoken[datum] = i

    next_up = data[-1]
    for turn in range(len(last_spoken) + 1, 2020):
        if next_up not in last_spoken:
            last_spoken[next_up] = turn
            next_up = 0
        else:
            next_next_up = turn - last_spoken[next_up]
            last_spoken[next_up] = turn
            next_up = next_next_up

    return next_up


def first(filename: Union[str, Path]) -> int:
    """
    Play a game where, after a starting sequence (the contents of filename),
    at each round the next value is:
        * 0 if the previous value had never been seen before
        * If the previous value had been seen in a previous round, the number
          of rounds between sightings

    Return the 2020th number to show up (inclusive of the starting sequence)
    """
    return play_game(filename, 2020)


def second(filename: Union[str, Path]) -> int:
    """
    Same as Part 1, but just go for 30m rounds. There's almost certainly
    a clever way to do this, but just running the program for 30m rounds
    doesn't actually take that long
    """
    return play_game(filename, 30_000_000)
