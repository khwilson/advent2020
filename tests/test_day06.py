from pathlib import Path

from advent import day06


def test_first(fixture_path: Path):
    assert day06.first(fixture_path / "example06.txt") == 11


def test_second(fixture_path: Path):
    assert day06.second(fixture_path / "example06.txt") == 6
