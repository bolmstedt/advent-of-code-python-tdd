import pytest

from aoc import loader
from aoc.year_2022.day_05_supply_stacks import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("[A] [B]\n 1   2\n\nmove 1 from 1 to 1", "AB"),
        (loader.get_module_data(solution, "fixture.txt"), "CMZ"),
        (loader.get_input_data(solution), "MQTPGLLDN"),
    ],
)
def test_moving_stacks_one_at_a_time(input_data: str, expected: str) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), "MCD"),
        (loader.get_input_data(solution), "LVZPSTTCZ"),
    ],
)
def test_moving_stacks_all_at_once(input_data: str, expected: str) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
