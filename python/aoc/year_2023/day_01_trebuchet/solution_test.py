import pytest

from aoc import loader
from aoc.year_2023.day_01_trebuchet import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("11", 11),
        ("1", 11),
        ("123", 13),
        ("a1b2c", 12),
        ("1\n2", 33),
        ("a1b2c\nd3e4f", 46),
        (loader.get_module_data(solution, "fixture.txt"), 142),
        (loader.get_input_data(solution), 55538),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("abc", 0),
        ("one", 11),
        ("twone", 21),
        (loader.get_module_data(solution, "fixture2.txt"), 281),
        (loader.get_input_data(solution), 54875),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
