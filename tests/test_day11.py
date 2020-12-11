from pathlib import Path

from advent import day11


def test_first(fixture_path: Path):
    assert day11.first(fixture_path / "example11.txt") == 37


def test_second(fixture_path: Path):
    assert day11.second(fixture_path / "example11.txt") == 26
