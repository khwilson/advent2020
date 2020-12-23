from pathlib import Path

import pytest

from advent import day23

def test_first(fixture_path: Path):
    assert day23.first(fixture_path / "example23.txt") == 67384529


@pytest.mark.skip("Takes way too long")
def test_second(fixture_path: Path):
    assert day23.second(fixture_path / "example23.txt") == 149245887792
