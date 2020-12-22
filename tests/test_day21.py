from pathlib import Path

from advent import day21


def test_first(fixture_path: Path):
    assert day21.first(fixture_path / "example21.txt") == 5


def test_second(fixture_path: Path):
    assert day21.second(fixture_path / "example21.txt") == "mxmxvkd,sqjhc,fvjkl"
