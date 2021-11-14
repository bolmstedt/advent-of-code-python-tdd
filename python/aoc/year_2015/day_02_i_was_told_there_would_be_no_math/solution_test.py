import pytest

from aoc import loader
from aoc.year_2015.day_02_i_was_told_there_would_be_no_math import solution


@pytest.mark.parametrize(
    ("test_data", "expected"),
    [
        ("1x1x1", 7),
        ("2x3x4", 58),
        ("1x1x10", 43),
        (loader.get_input_data(solution), 1586300),
    ],
)
def test_dimensions_require_expected_area(test_data: str, expected: int) -> None:
    assert solution.Solution(test_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("test_data", "expected"),
    [
        ("1x1x1", 5),
        ("2x3x4", 34),
        ("4x3x2", 34),
        ("1x1x10", 14),
        (loader.get_input_data(solution), 3737498),
    ],
)
def test_dimensions_require_expected_length(test_data: str, expected: int) -> None:
    assert solution.Solution(test_data).solve_part_two() == expected
