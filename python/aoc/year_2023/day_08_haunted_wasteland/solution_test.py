import pytest

from aoc import loader
from aoc.year_2023.day_08_haunted_wasteland import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        pytest.param(loader.get_module_data(solution, "fixture.txt"), 2, id="example"),
        pytest.param(loader.get_module_data(solution, "fixture2.txt"), 6, id="fixture"),
        pytest.param(loader.get_input_data(solution), 18113, id="solution"),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        pytest.param(loader.get_module_data(solution, "fixture3.txt"), 6, id="fixture"),
        pytest.param(loader.get_input_data(solution), 12315788159977, id="solution"),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
