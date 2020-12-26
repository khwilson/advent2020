""" AOC Day 12 """
from __future__ import annotations

from pathlib import Path
from typing import Union


class Coord:
    """
    Represent an x/y coordiate as a pair of ints. Also allow for
    adding and multiplying them pointwise.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __mul__(self, other: int) -> Coord:
        return Coord(self.x * other, self.y * other)

    def __add__(self, other: Coord) -> Coord:
        return Coord(self.x + other.x, self.y + other.y)


NORTH = Coord(0, 1)
SOUTH = Coord(0, -1)
EAST = Coord(1, 0)
WEST = Coord(-1, 0)


def _nsew(pos: Coord, cmd: str, val: int) -> Coord:
    if cmd == "N":
        return pos + NORTH * val
    if cmd == "S":
        return pos + SOUTH * val
    if cmd == "E":
        return pos + EAST * val
    if cmd == "W":
        return pos + WEST * val
    raise NotImplementedError(f"cmd must be one of N, S, E, or W, not {cmd}")


class Ship:
    """
    Perform the commands in absolute coordinates
    """

    def __init__(self):
        self.pos = Coord(0, 0)
        self.direction = EAST

    def step(self, cmd: str, val: int):
        if cmd in "NSEW":
            self.pos = _nsew(self.pos, cmd, val)
        if cmd == "L":
            while val > 0:
                self.direction = Coord(-self.direction.y, self.direction.x)
                val -= 90
        if cmd == "R":
            while val > 0:
                self.direction = Coord(self.direction.y, -self.direction.x)
                val -= 90
        if cmd == "F":
            self.pos = self.pos + self.direction * val


class Waypoint:
    """
    Perform the commands in relative coordinates
    """

    def __init__(self):
        self.pos = Coord(10, 1)
        self.abs_ship_pos = Coord(0, 0)

    def step(self, cmd: str, val: int):
        if cmd in "NSEW":
            self.pos = _nsew(self.pos, cmd, val)
        if cmd == "L":
            while val > 0:
                self.pos = Coord(-self.pos.y, self.pos.x)
                val -= 90
        if cmd == "R":
            while val > 0:
                self.pos = Coord(self.pos.y, -self.pos.x)
                val -= 90
        if cmd == "F":
            self.abs_ship_pos = self.abs_ship_pos + self.pos * val


def first(filename: Union[str, Path]) -> int:
    """
    Move a Ship according to the passed instructions
    """
    ship = Ship()
    with open(filename, "rt") as infile:
        for line in infile:
            line = line.strip()
            cmd = line[0]
            val = int(line[1:])
            ship.step(cmd, val)

    return abs(ship.pos.x) + abs(ship.pos.y)


def second(filename: Union[str, Path]) -> int:
    """
    Move a ship relatively to a Waypoint according to the instructions
    """
    waypoint = Waypoint()
    with open(filename, "rt") as infile:
        for line in infile:
            line = line.strip()
            cmd = line[0]
            val = int(line[1:])
            waypoint.step(cmd, val)

    return abs(waypoint.abs_ship_pos.x) + abs(waypoint.abs_ship_pos.y)
