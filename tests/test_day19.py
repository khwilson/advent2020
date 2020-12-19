from pathlib import Path

from advent import day19


def test_first(fixture_path: Path):
    day19.CS_MEMORY = {}
    assert day19.first(fixture_path / "example19.txt") == 2

    day19.CS_MEMORY = {}
    assert day19.first(fixture_path / "example192.txt") == 3


def test_second(fixture_path: Path):
    day19.CS_MEMORY = {}
    assert day19.second(fixture_path / "example192.txt") == 12
