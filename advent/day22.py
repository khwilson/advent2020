""" AOC Day 8 """
import copy
from collections import deque
from pathlib import Path
from typing import List, Union


def parse_file(filename: Union[str, Path]) -> List[List[int]]:
    with open(filename, "rt") as infile:
        raw_players = infile.read().split("\n\n")
        decks = [
            deque([int(card) for card in player.split("\n")[1:]])
            for player in raw_players
        ]

    # Make sure all the cards are distinct
    assert len({y for x in decks for y in x}) == sum(map(len, decks))

    return decks


def play_game(in_decks, do_recurse: bool = False):
    decks = copy.deepcopy(in_decks)
    seen_decks = set()
    while all(decks):
        left, right = decks[0].popleft(), decks[1].popleft()
        if do_recurse and len(decks[0]) >= left and len(decks[1]) >= right:
            winner, _ = play_game(
                [deque(list(decks[0])[:left]), deque(list(decks[1])[:right])],
                do_recurse=do_recurse,
            )
            if winner == 1:
                decks[0].extend([left, right])
            else:
                decks[1].extend([right, left])
            continue

        if left > right:
            decks[0].extend([left, right])
        elif right > left:
            decks[1].extend([right, left])
        else:
            raise ValueError("This cannot happen")

        tuple_decks = tuple(tuple(deck) for deck in decks)
        if tuple_decks in seen_decks:
            # player 1 wins by default
            return 1, decks
        seen_decks.add(tuple_decks)

    return (1 if decks[0] else 2), decks


def first(filename: Union[str, Path]) -> int:
    """
    Part 1
    """
    decks = parse_file(filename)
    _, decks = play_game(decks)

    winning_deck = decks[0] if decks[0] else decks[1]
    return sum(val * card for val, card in enumerate(reversed(winning_deck), 1))


def second(filename: Union[str, Path]) -> int:
    """
    Part 2
    """
    decks = parse_file(filename)

    _, final_decks = play_game(decks, do_recurse=True)
    winning_deck = final_decks[0] if final_decks[0] else final_decks[1]
    return sum(val * card for val, card in enumerate(reversed(winning_deck), 1))
