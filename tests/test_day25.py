from pathlib import Path

from advent import day25


def test_discrete_logarith():
    assert day25.disrete_logarithm((3 ** 13) % 17, 3, 17) == 13


def test_first(fixture_path: Path):
    assert day25.first(fixture_path / "example25.txt") == 14897079


# def test_second(fixture_path: Path):
#     assert day05.second(fixture_path / "example05.txt") == 241861950
