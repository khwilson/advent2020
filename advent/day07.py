""" AOC Day 7 """
import re
from collections import defaultdict, deque
from pathlib import Path
from typing import Dict, List, Tuple, Union


def parse_rules(filename: Union[str, Path]) -> Dict[str, List[Tuple[str, int]]]:
    """
    Parse the input text into a nice formatted set of rules. We assume:
        * Each type of bag appears on the left hand side of a rule
        * The rule list does not contain (directed) cycles
        * Each bag appears only once on the left hand side of a rule

    Input format:
        [BAG TYPE] bags contain (no other bags|[N] [BAG TYPE] bags?[, [N] [BAG TYPE] bags?...]).

    Output format:
        key: Left hand side bag type
        value: List of pairs (bag type, number of bags contained in
            parent bag of this type)
    """
    rules = {}
    with open(filename, "rt") as infile:
        for line in infile:
            line = line.strip("\n.")
            left, right = line.split("contain")
            left = left.strip()[: -len(" bags")]
            right = right.strip()
            all_right = right.split(",")
            children = []
            for thing in all_right:
                match = re.match(r"(\d+) ([a-z ]+) bags?", thing.strip())
                if not match:
                    if thing != "no other bags":
                        raise ValueError(f"Something is wrong in regex: {thing}")
                else:
                    children.append((match.groups()[1], int(match.groups()[0])))

            rules[left] = children
    return rules


def first(filename: Union[str, Path]) -> int:
    """
    How many types of bags can contain a shiny gold bag?
    """
    rules = parse_rules(filename)

    # Reverse rules so children point to parents
    child_to_parent = defaultdict(list)
    for key, value in rules.items():
        for child, _ in value:
            child_to_parent[child].append(key)

    # BFS up the tree
    seen_grandparents = set()
    queue = deque(["shiny gold"])

    # Shiny gold may not be allowed to be an outer bag unless it's
    # allowed to be empty
    if "shiny gold" in rules["shiny gold"] and len(rules["shiny gold"]) == 0:
        seen_grandparents.add("shiny gold")

    # Execute BFS
    while queue:
        bag = queue.popleft()
        for parent in child_to_parent[bag]:
            if parent not in seen_grandparents:
                seen_grandparents.add(parent)
                queue.append(parent)

    return len(seen_grandparents)


def count_bags(
    rules: Dict[str, List[Tuple[str, int]]], bag_name: str, multiplier: int
) -> int:
    """
    Count the number of bags necessarily contained in `multipler` bags of
    type `bag_name` according to the `rules`.

    Note that this includes the outer bags themselves!
    """
    return multiplier * (
        1 + sum(count_bags(rules, name, mult) for name, mult in rules[bag_name])
    )


def second(filename: Union[str, Path]) -> int:
    """
    How many bags are contained in a shiny gold bag, not including the
    shiny gold bag itself?
    """
    rules = parse_rules(filename)

    # -1 because we're not counting the outer shiny gold bag itself
    return count_bags(rules, "shiny gold", 1) - 1
