""" AOC Day 3 """
from pathlib import Path
from typing import List, Union

TREE = "#"
OPEN = "."


def parse_file(filename: Union[str, Path]) -> List[str]:
    """ Parse the file contents """
    with open(filename, "rt") as infile:
        return [line.strip() for line in infile]


def count_trees(spaces: List[str], right: int = 3, down: int = 1) -> int:
    """
    Count the number of TREEs in the spaces map when going down a slope that
    is `right` steps to the right and `down` steps down.
    """
    total_trees = 0
    for i, row in enumerate(spaces[::down]):
        total_trees += row[(right * i) % len(row)] == TREE
    return total_trees


def first(filename: Union[str, Path]) -> int:
    """
    Count the number of TREEs you hit going at a slope of 3 right and 1 down
    """
    spaces = parse_file(filename)
    return count_trees(spaces)


def second(filename: Union[str, Path]) -> int:
    """
    Return the product of the number of tress hit along several slopes
    """
    spaces = parse_file(filename)
    return (
        count_trees(spaces, 1, 1)
        * count_trees(spaces, 3, 1)
        * count_trees(spaces, 5, 1)
        * count_trees(spaces, 7, 1)
        * count_trees(spaces, 1, 2)
    )
