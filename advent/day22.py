""" AOC Day 8 """
import copy
from collections import deque
from pathlib import Path
from typing import List, Tuple, Union


def parse_file(filename: Union[str, Path]) -> Tuple[deque, deque]:
    """
    Parse the incoming file. The output is a pair of lists of ints representing
    the starting hands for the game that is played in `play_game`.
    """
    with open(filename, "rt") as infile:
        raw_players = infile.read().split("\n\n")
        decks = tuple(
            [
                deque([int(card) for card in player.split("\n")[1:]])
                for player in raw_players
            ]
        )

    # Make sure all the cards are distinct
    assert len({y for x in decks for y in x}) == sum(map(len, decks))

    # Make sure there are two players
    assert len(decks) == 2

    return decks


def play_game(
    in_decks: Tuple[List[int], List[int]], do_recurse: bool = False
) -> Tuple[int, Tuple[List[int], List[int]]]:
    """
    Play a game of war, with a weird recursive subgame if `do_recurse` is True.

    Return:
        * The winner of the game (either 1 or 2, corresponds to the
          first or second deck of in_decks)
        * The final state of the decks after the game is over
    """
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
    Play a game of war
    """
    decks = parse_file(filename)
    _, decks = play_game(decks)

    winning_deck = decks[0] if decks[0] else decks[1]
    return sum(val * card for val, card in enumerate(reversed(winning_deck), 1))


def second(filename: Union[str, Path]) -> int:
    """
    Play a game of war with some quirks
    """
    decks = parse_file(filename)

    _, final_decks = play_game(decks, do_recurse=True)
    winning_deck = final_decks[0] if final_decks[0] else final_decks[1]
    return sum(val * card for val, card in enumerate(reversed(winning_deck), 1))
