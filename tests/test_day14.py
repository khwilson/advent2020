from pathlib import Path

from advent import day14


def test_first(fixture_path: Path):
    assert day14.first(fixture_path / "example14.txt") == 165


def test_second(fixture_path: Path):
    assert day14.second(fixture_path / "example142.txt") == 208
