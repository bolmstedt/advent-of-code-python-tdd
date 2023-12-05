import pytest

from aoc import loader
from aoc.year_2023.day_02_cube_conundrum import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("Game 1: 1 red", 1),
        ("Game 1: 13 red", 0),
        ("Game 1: 1 blue, 1 green, 1 red", 1),
        ("Game 1: 1 blue, 1 green, 1 red; 2 blue, 2 green, 2 red", 1),
        (loader.get_module_data(solution, "fixture.txt"), 8),
        (loader.get_input_data(solution), 2085),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("Game 1: 1 blue, 1 green, 1 red", 1),
        ("Game 1: 2 blue, 2 green, 2 red", 8),
        ("Game 1: 2 blue; 2 green; 2 red", 8),
        (
            "Game 1: 2 blue, 1 green, 1 red; 1 blue, 2 green, 1 red; 1 blue, 1 green, 2 red",
            8,
        ),
        (loader.get_module_data(solution, "fixture.txt"), 2286),
        (loader.get_input_data(solution), 79315),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
