""" AOC Day 8 """
import itertools as its
import operator
import re
from functools import reduce
from pathlib import Path
from typing import Dict, List, Set, Tuple, Union

RuleType = List[Union[str, Tuple[int, ...]]]


def parse_input(filename: Union[str, Path]) -> Tuple[Dict[int, RuleType], List[str]]:
    rules = {}
    strings = []
    with open(filename, "rt") as infile:
        # Parse the rules
        for line in infile:
            line = line.strip()
            if not line:
                # This is the end of the rule list
                break
            rule_id, rule = line.strip().split(": ")

            if rule == '"a"':
                rule = "a"
            elif rule == '"b"':
                rule = "b"
            else:
                sub_rules = rule.split(" | ")
                rule = []
                for sub_rule in sub_rules:
                    rule.append(tuple(map(int, re.findall(r"\d+", sub_rule))))
            rules[int(rule_id)] = rule

        # Parse the strings
        for line in infile:
            strings.append(line.strip())

    return rules, strings


# Memoizer for `construct_strings`. Memoized on `rule_id`
# since we assume `rules` is constant
CS_MEMORY: Dict[int, Set[str]] = {}


def construct_strings(rules: Dict[int, RuleType], rule_id: int) -> Set[str]:
    """
    Construct all valid strings that match rule `rule_id`. Note that this
    only works if ther are no loops in the input
    """
    if rule_id in CS_MEMORY:
        return CS_MEMORY[rule_id]

    final = set()
    for rule in rules[rule_id]:
        if isinstance(rule, str):
            final.add(rule)
            break

        outputs = []
        for sub_rule_id in rule:
            outputs.append(construct_strings(rules, sub_rule_id))

        final |= {reduce(operator.add, output, "") for output in its.product(*outputs)}

    CS_MEMORY[rule_id] = final
    return final


def regex(
    rules: Dict[int, RuleType], rule_id: int, cur_depth: int, max_depth: int
) -> str:
    """
    Recursively construct a regular expression that matches rule `rule_id`. Note that
    since we're trying to match a fixed set of strings, we bound the depth of our
    recursion with cur_depth and max_depth.
    """
    if cur_depth > max_depth:
        return ""

    re_rules = []
    for rule in rules[rule_id]:
        if isinstance(rule, str):
            re_rules.append(rule)
        else:
            next_rules = [
                regex(rules, sub_rule_id, cur_depth + 1, max_depth)
                for sub_rule_id in rule
            ]
            re_rules.append(reduce(operator.add, next_rules, ""))
    return f'({"|".join(re_rules)})'


def first(filename: Union[str, Path]) -> int:
    """
    Match strings according to a set of rules with no loops
    """
    rules, strings = parse_input(filename)

    # Be lazy and generate all valid substrings (but don't forget to memoize)
    valid_strings = construct_strings(rules, 0)
    return sum(string in valid_strings for string in strings)


def second(filename: Union[str, Path]) -> int:
    """
    Match strings according to a set of rules with loops
    """
    rules, strings = parse_input(filename)

    # The prompt says change some of the input
    rules[8] = [(42,), (42, 8)]
    rules[11] = [(42, 31), (42, 11, 31)]

    reg = re.compile(regex(rules, 0, 0, max(map(len, strings)) + 1))
    return sum(bool(reg.fullmatch(string)) for string in strings)
