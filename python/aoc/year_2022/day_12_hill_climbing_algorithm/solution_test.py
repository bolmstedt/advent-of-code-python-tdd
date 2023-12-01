import string

import pytest

from aoc import loader
from aoc.year_2022.day_12_hill_climbing_algorithm import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("S{alpha}E".format(alpha=string.ascii_lowercase[1:-1]), 25),
        (loader.get_module_data(solution, "fixture.txt"), 31),
        (loader.get_input_data(solution), 504),
    ],
)
def test_monkey_business(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 29),
        (loader.get_input_data(solution), 500),
    ],
)
def test_more_monkey_business(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
