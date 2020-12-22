from pathlib import Path

from advent import day22


def test_first(fixture_path: Path):
    assert day22.first(fixture_path / "example22.txt") == 306


def test_second(fixture_path: Path):
    assert day22.second(fixture_path / "example22.txt") == 291
