from pathlib import Path

from advent import day12


def test_first(fixture_path: Path):
    assert day12.first(fixture_path / "example12.txt") == 25


def test_second(fixture_path: Path):
    assert day12.second(fixture_path / "example12.txt") == 286
