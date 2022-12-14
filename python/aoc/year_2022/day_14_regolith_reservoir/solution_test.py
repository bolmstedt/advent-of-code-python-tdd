import pytest

from aoc import loader
from aoc.year_2022.day_14_regolith_reservoir import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 24),
        (loader.get_input_data(solution), 737),
    ],
)
def test_sand(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 93),
        (loader.get_input_data(solution), 28145),
    ],
)
def test_safe_place(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
