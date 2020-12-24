from pathlib import Path

from advent import day24


def test_first(fixture_path: Path):
    assert day24.first(fixture_path / "example24.txt") == 10


def test_second(fixture_path: Path):
    assert day24.second(fixture_path / "example24.txt") == 2208
