from pathlib import Path

from advent import day05


def test_convert_all():
    assert day05.convert_all("FBFBBFFRLR") == 357
    assert day05.convert_all("BFFFBBFRRR") == 567
    assert day05.convert_all("FFFBBBFRRR") == 119
    assert day05.convert_all("BBFFBBFRLL") == 820


def test_first(fixture_path: Path):
    assert day05.first(fixture_path / "example05.txt") == 820
