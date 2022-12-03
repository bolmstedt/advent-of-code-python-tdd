import pytest

from aoc import loader
from aoc.year_2022.day_03_rucksack_reorganization import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("aa", 1),
        ("AA", 27),
    ],
)
def test_priority(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("abad", 1),
        ("adcd", 4),
    ],
)
def test_compartments(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 157),
        (loader.get_input_data(solution), 8039),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 70),
        (loader.get_input_data(solution), 2510),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
