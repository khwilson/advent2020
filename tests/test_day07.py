from pathlib import Path

from advent import day07


def test_first(fixture_path: Path):
    assert day07.first(fixture_path / "example07.txt") == 4


def test_second(fixture_path: Path):
    assert day07.second(fixture_path / "example07.txt") == 32
    assert day07.second(fixture_path / "example072.txt") == 126
