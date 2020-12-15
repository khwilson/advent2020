from pathlib import Path

from advent import day15


def test_first(fixture_path: Path):
    assert day15.first(fixture_path / "example15.txt") == 1
    assert day15.first(fixture_path / "example153.txt") == 10


# def test_second(fixture_path: Path):
#     assert day15.second(fixture_path / "example15.txt") == 241861950
