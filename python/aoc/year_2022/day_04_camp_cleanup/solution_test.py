import pytest

from aoc import loader
from aoc.year_2022.day_04_camp_cleanup import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("1-1,2-2", 0),
        ("1-3,2-2", 1),
        ("2-2,1-3", 1),
        (loader.get_module_data(solution, "fixture.txt"), 2),
        (loader.get_input_data(solution), 599),
    ],
)
def test_maximum_calories(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("1-1,2-2", 0),
        ("1-2,2-3", 1),
        ("2-3,1-2", 1),
        (loader.get_module_data(solution, "fixture.txt"), 4),
        (loader.get_input_data(solution), 928),
    ],
)
def test_combined_calories(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
