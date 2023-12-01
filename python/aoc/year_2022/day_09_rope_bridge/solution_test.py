import pytest

from aoc import loader
from aoc.year_2022.day_09_rope_bridge import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("R 2", 2),
        ("L 2", 2),
        ("U 2", 2),
        ("D 2", 2),
        ("R 1\nD 1\nR 1", 2),
        (loader.get_module_data(solution, "fixture.txt"), 13),
        (loader.get_input_data(solution), 5779),
    ],
)
def test_short_rope(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 1),
        (loader.get_module_data(solution, "fixture2.txt"), 36),
        (loader.get_input_data(solution), 2331),
    ],
)
def test_long_rope(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
