from pathlib import Path

from advent import day20


def test_first(fixture_path: Path):
    assert day20.first(fixture_path / "example20.txt") == 20899048083289


def test_second(fixture_path: Path):
    assert day20.second(fixture_path / "example20.txt") == 273
