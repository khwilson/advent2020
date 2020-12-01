from pathlib import Path

from advent import day01


def test_first(fixture_path: Path):
    assert day01.first(fixture_path / "example01.txt") == 514579


def test_second(fixture_path: Path):
    assert day01.second(fixture_path / "example01.txt") == 241861950
