""" AOC Day 21 """
import copy
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Set, Tuple, Union


def parse_file(
    filename: Union[str, Path]
) -> Tuple[Dict[str, Set[str]], Dict[str, int]]:
    """
    Parse the set of allergens attached to various collections of foods
    """
    lines = []
    with open(filename, "rt") as infile:
        for line in infile:
            line = line.strip().rstrip(")")
            left, _, right = line.partition(" (contains ")
            ingredients = left.split(" ")
            allergens = right.split(", ") if right else []
            lines.append((ingredients, allergens))

    foods = {food for line in lines for food in line[0]}

    allergen_to_foods: Dict[str, Set[str]] = defaultdict(lambda: copy.copy(foods))
    for food_list, allergen_list in lines:
        for allergen in allergen_list:
            allergen_to_foods[allergen] &= set(food_list)

    ingredient_count = Counter(food for foods, _ in lines for food in foods)
    return allergen_to_foods, ingredient_count


def first(filename: Union[str, Path]) -> int:
    """
    Part 1
    """
    allergen_to_foods, ingredient_count = parse_file(filename)
    return sum(
        ingredient_count[food]
        for food in ingredient_count
        if not any(food in val for val in allergen_to_foods.values())
    )


def second(filename: Union[str, Path]) -> int:
    """
    Part 2
    """
    allergen_to_foods, _ = parse_file(filename)

    assigned_allergens = {}
    allergen_to_foods = list(allergen_to_foods.items())
    while allergen_to_foods:
        allergen_to_foods.sort(key=lambda kv: len(kv[1]))
        allergen, foods = allergen_to_foods[0]

        assert len(foods) == 1
        food = list(foods)[0]
        assigned_allergens[allergen] = food
        allergen_to_foods = [(key, val - foods) for key, val in allergen_to_foods[1:]]

    return ",".join(
        y[1] for y in sorted(assigned_allergens.items(), key=lambda x: x[0])
    )
