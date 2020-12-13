from pathlib import Path

from advent import day13


def test_first(fixture_path: Path):
    assert day13.first(fixture_path / "example13.txt") == 295


def test_second(fixture_path: Path):
    assert day13.second(fixture_path / "example13.txt") == 1068781
