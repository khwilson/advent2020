from pathlib import Path

from advent import day18


def test_first(fixture_path: Path):
    assert day18.first(fixture_path / "example18.txt") == 71 + 51


def test_second(fixture_path: Path):
    assert day18.second(fixture_path / "example18.txt") == 231 + 51
