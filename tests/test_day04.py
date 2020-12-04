from pathlib import Path

from advent import day04


def test_first(fixture_path: Path):
    assert day04.first(fixture_path / "example04.txt") == 2


def test_second(fixture_path: Path):
    assert day04.second(fixture_path / "example042.txt") == 5
