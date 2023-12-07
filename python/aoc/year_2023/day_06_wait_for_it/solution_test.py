import pytest

from aoc import loader
from aoc.year_2023.day_06_wait_for_it import solution


@pytest.mark.parametrize(
    ("race", "expected"),
    [
        (solution.Race(limit=7, record=9), 4),
        (solution.Race(limit=15, record=40), 8),
        (solution.Race(limit=30, record=200), 9),
        (solution.Race(limit=71530, record=940200), 71503),
    ],
)
def test_ways_to_win(race: solution.Race, expected: int) -> None:
    assert solution.ways_to_win(race) == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 288),
        (loader.get_input_data(solution), 1083852),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 71503),
        (loader.get_input_data(solution), 23501589),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
