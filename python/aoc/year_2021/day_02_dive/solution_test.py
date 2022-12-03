import pytest

from aoc import loader
from aoc.year_2021.day_02_dive import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("forward 1", 0),
        ("down 1", 0),
        ("up 1", 0),
        ("up 1\nforward 1", -1),
        ("down 1\nforward 1", 1),
        (loader.get_module_data(solution, "fixture.txt"), 150),
    ],
)
def test_coordinates(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("forward 1", 0),
        ("down 1", 0),
        ("up 1", 0),
        ("up 1\nforward 1", -1),
        ("down 1\nforward 1", 1),
        ("down 2\nforward 2", 8),
        (loader.get_module_data(solution, "fixture.txt"), 900),
    ],
)
def test_complex_coordinates(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
