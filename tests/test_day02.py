from pathlib import Path

from advent import day02


def test_first(fixture_path: Path):
    assert day02.first(fixture_path / "example02.txt") == 2


def test_second(fixture_path: Path):
    assert day02.second(fixture_path / "example02.txt") == 1
