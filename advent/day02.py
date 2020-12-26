""" AOC Day 2 """
import re
from pathlib import Path
from typing import Tuple, Union


def _extract_values(line: str) -> Tuple[int, int, str, str]:
    match = re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", line.strip())
    if not match:
        raise ValueError(f"line does not conform to rules: {line}")
    left, right, letter, password = match.groups()
    return int(left), int(right), letter, password


def first(filename: Union[str, Path]) -> int:
    """
    Each line of the file looks like::

        number-number letter: string

    Return the total number of lines where the number of times
    that letter appears in string is between the two numbers
    (inclusive)
    """
    total_valid = 0
    with open(filename, "rt") as infile:
        for line in infile:
            policy_min, policy_max, letter, password = _extract_values(line)
            count = sum(1 for let in password if let == letter)
            if policy_min <= count <= policy_max:
                total_valid += 1
    return total_valid


def second(filename: Union[str, Path]) -> int:
    """
    Each line of the file looks like::

        number-number letter: string

    Return the total number of lines where exactly one of the
    (first or second number)th character of the string (1 indexed)
    is letter
    """
    total_valid = 0
    with open(filename, "rt") as infile:
        for line in infile:
            pos_one, pos_two, letter, password = _extract_values(line)
            if (password[pos_one - 1] == letter) != (password[pos_two - 1] == letter):
                total_valid += 1
    return total_valid
