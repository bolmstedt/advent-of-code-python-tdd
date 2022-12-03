import pytest

from aoc import loader
from aoc.year_2022.day_01_calorie_counting import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("1", 1),
        ("2\n1", 3),
        ("2\n\n1", 2),
        (loader.get_module_data(solution, "fixture.txt"), 24000),
        (loader.get_input_data(solution), 68787),
    ],
)
def test_maximum_calories(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("1\n\n1\n\n1", 3),
        ("1\n\n1\n\n1\n\n2", 4),
        (loader.get_module_data(solution, "fixture.txt"), 45000),
        (loader.get_input_data(solution), 198041),
    ],
)
def test_combined_calories(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
