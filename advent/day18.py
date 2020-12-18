""" AOC Day 8 """
import re
from pathlib import Path
from typing import Union


def first(filename: Union[str, Path]) -> int:
    """
    Evaluate arithmetic expressions where the precedence of + and * are the same
    """
    total = 0
    with open(filename, "rt") as infile:
        for line in infile:
            parts = line.strip().replace("(", " ( ").replace(")", " ) ").split()
            stack = []
            for part in parts:
                if part.isdigit():
                    if stack:
                        if stack[-1] == "*":
                            stack.pop()
                            stack[-1] *= int(part)
                        elif stack[-1] == "+":
                            stack.pop()
                            stack[-1] += int(part)
                        else:
                            stack.append(int(part))
                    else:
                        stack.append(int(part))
                else:
                    if part in "*+(":
                        stack.append(part)
                    elif part == ")":
                        assert stack[-2] == "("
                        stack[-1] = stack.pop()
                        while len(stack) > 1 and stack[-2] in "*+":
                            if stack[-2] == "+":
                                stack[-3] += stack[-1]
                                stack.pop()
                                stack.pop()
                            else:
                                stack[-3] *= stack[-1]
                                stack.pop()
                                stack.pop()

                    else:
                        raise ValueError
            assert len(stack) == 1
            total += stack[0]
    return total


class Reverser:
    """ Reverse the order of operations of + and * """

    def __init__(self, val: int):
        self.val = val

    def __add__(self, other):
        return Reverser(self.val * other.val)

    def __radd__(self, other):
        return Reverser(self.val * other.val)

    def __mul__(self, other):
        return Reverser(self.val + other.val)

    def __rmul__(self, other):
        return Reverser(self.val + other.val)

    def __str__(self):
        return str(self.val)


def second(filename: Union[str, Path]) -> int:
    """
    Evaluate arithmetic expressions where the precedence of + and * are reversed
    We do this the hacky way by wrapping ints in a Reverser class that
    implements different +/* methods
    """
    total = 0
    with open(filename, "rt") as infile:
        for line in infile:
            line = re.sub(r"(\d+)", r"Reverser(\g<1>)", line.strip())
            line = line.replace("+", "^")
            line = line.replace("*", "+")
            line = line.replace("^", "*")
            total += eval(line).val
    return total
