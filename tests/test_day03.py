from pathlib import Path

from advent import day03


def test_first(fixture_path: Path):
    assert day03.first(fixture_path / "example03.txt") == 7


def test_second(fixture_path: Path):
    assert day03.second(fixture_path / "example03.txt") == 336
