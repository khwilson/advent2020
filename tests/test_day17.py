from pathlib import Path

import pytest

from advent import day17


def test_first(fixture_path: Path):
    assert day17.first(fixture_path / "example17.txt") == 112


@pytest.mark.skip("This test takes a long time")
def test_second(fixture_path: Path):
    assert day17.second(fixture_path / "example17.txt") == 848
