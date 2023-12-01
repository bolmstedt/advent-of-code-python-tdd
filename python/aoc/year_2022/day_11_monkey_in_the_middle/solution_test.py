import pytest

from aoc import loader
from aoc.year_2022.day_11_monkey_in_the_middle import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 10605),
        (loader.get_input_data(solution), 78960),
    ],
)
def test_monkey_business(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 2713310158),
        (loader.get_input_data(solution), 14561971968),
    ],
)
def test_more_monkey_business(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
