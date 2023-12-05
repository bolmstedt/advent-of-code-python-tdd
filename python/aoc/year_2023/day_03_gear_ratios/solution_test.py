import pytest

from aoc import loader
from aoc.year_2023.day_03_gear_ratios import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("1.1", 0),
        ("1*1", 2),
        ("2#3", 5),
        ("1.1\n.@.\n1.1", 4),
        ("1.$1", 1),
        (loader.get_module_data(solution, "fixture.txt"), 4361),
        (loader.get_input_data(solution), 527369),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("1.1", 0),
        ("1*1", 1),
        ("1.*.1", 0),
        ("1*.1", 0),
        ("1.*1", 0),
        ("1.1\n.*.\n...", 1),
        (".1.\n.*.\n.1.", 1),
        ("1.1\n.*.\n1.1", 0),
        ("1..\n.*.\n1..", 1),
        ("..1\n.*.\n..1", 1),
        ("1..\n..*\n1..", 0),
        ("..1\n*..\n..1", 0),
        ("123\n..*\n456", 56088),
        ("123\n*..\n456", 56088),
        ("123\n.*.\n456", 56088),
        (loader.get_module_data(solution, "fixture.txt"), 467835),
        (loader.get_input_data(solution), 73074886),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
