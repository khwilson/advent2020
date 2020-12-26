from pathlib import Path

from advent import day16


def test_first(fixture_path: Path):
    assert day16.first(fixture_path / "example16.txt") == 71
