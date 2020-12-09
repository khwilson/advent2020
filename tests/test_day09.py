from pathlib import Path

from advent import day09


def test_first(fixture_path: Path):
    assert day09.first(fixture_path / "example09.txt", preamble_length=5) == 127


def test_second(fixture_path: Path):
    assert day09.second(fixture_path / "example09.txt", preamble_length=5) == 62
