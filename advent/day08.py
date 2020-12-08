""" AOC Day 8 """
from __future__ import annotations

import copy
from collections import deque
from pathlib import Path
from typing import List, Union


class CodeRunner:
    """
    A class that holds an instruction set and the state of the machine that
    runs it.
    """

    def __init__(self, instructions: List[str, int]):
        self.instructions = instructions
        self.acc = 0
        self.pc = 0

    @classmethod
    def parse_file(cls, filename: Union[str, Path]) -> CodeRunner:
        """
        Parse a text file of instructions into a `CodeRunner` object
        """
        instructions: List[str, int] = []
        with open(filename, "rt") as infile:
            for line in infile:
                inst, val = line.strip().split()

                # Values start with + or -
                val = int(val) if val.startswith("-") else int(val[1:])
                instructions.append((inst, val))
        return cls(instructions)

    def step(self):
        """
        Execute the current instruction and increment the program counter or jump
        """
        inst, val = self.instructions[self.pc]
        if inst == "acc":
            self.acc += val
            self.pc += 1
        elif inst == "jmp":
            self.pc += val
        elif inst == "nop":
            self.pc += 1
        else:
            raise ValueError(f"Bad instruction: {inst}")

    def run(self):
        """
        While the program counter points to a valid instruction, take a step
        """
        while self.pc < len(self.instructions):
            self.step()

    def __repr__(self) -> str:
        return f"<CodeRunner(pc={self.pc}, acc={self.acc})>"


def first(filename: Union[str, Path]) -> int:
    """
    Find the value of the accumulator right before an instruction is
    executed for the second time.
    """
    runner = CodeRunner.parse_file(filename)
    seen_pcs = set()
    while True:
        if runner.pc in seen_pcs:
            break
        seen_pcs.add(runner.pc)
        runner.step()
    return runner.acc


def second(filename: Union[str, Path]) -> int:
    """
    Change a single jmp or nop instruction (but not the value) into a nop or jmp
    so that the passed program actually terminates right after it executes the
    last instruction in the list.

    Strategy:
        * Find all the instructions that if you ran the program would eventually
          reach the final instruction
        * Run the program from the start, checking at each step whether
          switching nop <-> jmp would cause the program to step to a grandparent
          instruction of the final instruction
        * If so, change the instruction and then execute the program to completion

    Returns:
        The accumulator value upon the program's termination
    """
    runner = CodeRunner.parse_file(filename)

    # Make a graph of the instruction set
    children = [[] for _ in range(len(runner.instructions))]
    parents = [[] for _ in range(len(runner.instructions))]
    for pc, (inst, val) in enumerate(runner.instructions):
        if inst in ["nop", "acc"]:
            if pc + 1 < len(runner.instructions):
                children[pc].append(pc + 1)
                parents[pc + 1].append(pc)
        elif inst == "jmp":
            if pc + val < len(runner.instructions):
                children[pc].append(pc + val)
                parents[pc + val].append(pc)
        else:
            raise ValueError(f"Bad instruction: {inst}")

    # Get all grandparents of the last instruction
    grandparents = set()
    queue = deque([len(runner.instructions) - 1])
    while queue:
        pc = queue.popleft()
        if pc not in grandparents:
            grandparents.add(pc)
            queue.extend(parents[pc])

    # Now try running the program
    seen_pcs = set()
    while True:
        if runner.pc in seen_pcs:
            raise ValueError("Didn't win")
        seen_pcs.add(runner.pc)

        inst, val = runner.instructions[runner.pc]
        if inst == "jmp":
            # Check if the next instruction is in the grandparent set
            if runner.pc + 1 in grandparents:
                runner.instructions[runner.pc] = ("nop", val)
                break
        elif inst == "nop":
            # Check if the indicated jmp location is in the grandparent set
            if runner.pc + val in grandparents:
                runner.instructions[runner.pc] = ("jmp", val)
                break

        runner.step()

    runner.run()
    return runner.acc
