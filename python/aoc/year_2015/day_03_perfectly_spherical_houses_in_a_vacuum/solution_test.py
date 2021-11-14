import pytest

from aoc import loader
from aoc.year_2015.day_03_perfectly_spherical_houses_in_a_vacuum import solution


@pytest.mark.parametrize(
    ("test_data", "expected"),
    [
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
        (loader.get_input_data(solution), 2565),
    ],
)
def test_dimensions_require_expected_area(test_data: str, expected: int) -> None:
    assert solution.Solution(test_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("test_data", "expected"),
    [
        ("^v", 3),
        ("^>v<", 3),
        ("^v^v^v^v^v", 11),
        (loader.get_input_data(solution), 2639),
    ],
)
def test_dimensions_require_expected_length(test_data: str, expected: int) -> None:
    assert solution.Solution(test_data).solve_part_two() == expected
