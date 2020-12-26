""" AOC Day 13 """
from pathlib import Path
from typing import Union


def first(filename: Union[str, Path]) -> int:
    """
    For each bus_id, look for the smallest multiple of bus_id greater than
    earliest_timestamp.

    Among all these multiples, let M be the closest to earliest_timestamp
    belonging to bus_id. Return (M - earliest_timestamp) * bus_id
    """
    with open(filename, "rt") as infile:
        earliest_timestamp = int(next(infile).strip())
        buses_in_services = [
            int(x) for x in next(infile).strip().split(",") if x != "x"
        ]

    # Just make sure that there a no buses with a 0 minute wait time
    for bus_id in buses_in_services:
        if earliest_timestamp % bus_id == 0:
            return 0

    # Else, the wait time is bus_id - (earliest_timestamp % bus_id)
    wait_time, bus_id = min(
        (bus_id - (earliest_timestamp % bus_id), bus_id) for bus_id in buses_in_services
    )
    return wait_time * bus_id


def second(filename: Union[str, Path]) -> int:
    """
    Consider the collection of integers n_i at position r_i in the input
    (0-delimited). Then solve the system of congruences x ≡ -r_i (mod n_i)
    """
    with open(filename, "rt") as infile:
        next(infile)
        buses_in_services = [
            (int(x) - (mod % int(x)), int(x))
            for mod, x in enumerate(next(infile).strip().split(","))
            if x != "x"
        ]

    # Perform the Chinese Remainder Theorem. Note that this works
    # because everything is prime
    cur_val, cur_mod = buses_in_services[0]
    for next_rem, next_mod in buses_in_services[1:]:
        val = cur_val
        while val % next_mod != next_rem:
            val += cur_mod

        cur_val = val
        cur_mod *= next_mod

    return cur_val
