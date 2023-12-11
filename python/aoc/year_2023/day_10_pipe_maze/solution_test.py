import pytest

from aoc import loader
from aoc.year_2023.day_10_pipe_maze import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("S7\nLJ", 2),
        ("-S7\n.LJ", 2),
        pytest.param(loader.get_module_data(solution, "fixture.txt"), 4, id="fixture"),
        pytest.param(
            loader.get_module_data(solution, "fixture2.txt"),
            8,
            id="fixture2",
        ),
        pytest.param(loader.get_input_data(solution), 6714, id="solution"),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("S7\nLJ", 0),
        (loader.get_module_data(solution, "fixture.txt"), 1),
        (loader.get_module_data(solution, "fixture2.txt"), 1),
        (loader.get_module_data(solution, "fixture3.txt"), 4),
        (loader.get_module_data(solution, "fixture4.txt"), 4),
        (loader.get_module_data(solution, "fixture5.txt"), 8),
        (loader.get_module_data(solution, "fixture6.txt"), 10),
        pytest.param(loader.get_input_data(solution), 429, id="solution"),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
