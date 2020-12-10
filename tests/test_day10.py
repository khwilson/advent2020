from pathlib import Path

from advent import day10


def test_first(fixture_path: Path):
    assert day10.first(fixture_path / "example101.txt") == 7 * 5
    assert day10.first(fixture_path / "example102.txt") == 22 * 10


def test_second(fixture_path: Path):
    assert day10.second(fixture_path / "example101.txt") == 8
    assert day10.second(fixture_path / "example102.txt") == 19208
