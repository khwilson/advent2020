""" AOC Day 16 """
import itertools as its
import re
from pathlib import Path
from typing import List, Tuple, Union

import numpy as np


def get_ranges_and_departures(
    header: str,
) -> Tuple[List[List[Tuple[int, int]]], List[int]]:
    """
    Parse the header of the incoming data. It's formatted as::

        name: #-#[ or #-# [...]]

    Return the list of tuples of ranges formatted as [[(#, #), (#, #)], ...]
    and the list of row indices that start with the word 'departure' for Part 2
    """
    ranges = []
    departure_lines = []

    for i, line in enumerate(header.split("\n")):
        if line.startswith("departure"):
            departure_lines.append(i)
        raw_ranges = re.findall(r"(\d+)", line)
        ranges.append(
            [
                (int(left), int(right))
                for left, right in zip(raw_ranges[::2], raw_ranges[1::2])
            ]
        )

    return ranges, departure_lines


def first(filename: Union[str, Path]) -> int:
    """
    Some numbers in the third section do not fit in any valid range.
    Return the sum of those completely invalid numbers.
    """
    with open(filename, "rt") as infile:
        header, _, nearby_tickets = infile.read().strip().split("\n\n")

    ranges, _ = get_ranges_and_departures(header)

    return sum(
        int(num)
        for ticket in nearby_tickets.split("\n")[1:]
        for num in ticket.split(",")
        if not any(left <= int(num) <= right for left, right in its.chain(*ranges))
    )


def second(filename: Union[str, Path]) -> int:
    """
    Many steps:
        1. Throw out the rows in the third section of the input that have a number
           that falls in no enumerated range in the top section
        2. Deduce which row in the header corresponds to which column in third secion
        3. Return the product of the "departure" relevant columns in the second section
    """
    with open(filename, "rt") as infile:
        header, my_ticket, nearby_tickets = infile.read().strip().split("\n\n")

    ranges, departure_lines = get_ranges_and_departures(header)

    valid_tickets: List[Tuple[int]] = [
        tuple(map(int, ticket.split(",")))
        for ticket in nearby_tickets.split("\n")[1:]
        if all(
            any(left <= int(num) <= right for left, right in its.chain(*ranges))
            for num in ticket.split(",")
        )
    ]

    # Might be able to save time by keeping these as sets, but the input
    # isn't huge and it's easy enough to write all this out in numpy
    order_to_description = np.ones((len(ranges), len(ranges)), dtype=bool)

    for ticket in valid_tickets:
        for i, val in enumerate(ticket):
            for j in np.where(order_to_description[i, :])[0]:
                order_to_description[i, j] = any(
                    left <= val <= right for left, right in ranges[j]
                )

    for i in np.argsort(order_to_description.sum(axis=1)):
        order_to_description[:i, :] &= ~order_to_description[i, :]
        order_to_description[i + 1 :, :] &= ~order_to_description[i, :]

    my_ticket = list(map(int, my_ticket.strip().split("\n")[1].split(",")))

    # Note that in determining the label attached to a given value,
    # we need to take the _transpose_ of the matrix
    total = 1
    for i in departure_lines:
        total *= my_ticket[np.where(order_to_description[:, i])[0][0]]

    return total
