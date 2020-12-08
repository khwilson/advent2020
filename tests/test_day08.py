from pathlib import Path

from advent import day08


def test_first(fixture_path: Path):
    assert day08.first(fixture_path / "example08.txt") == 5


def test_second(fixture_path: Path):
    assert day08.second(fixture_path / "example08.txt") == 8
