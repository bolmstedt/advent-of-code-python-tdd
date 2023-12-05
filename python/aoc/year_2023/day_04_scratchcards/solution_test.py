import pytest

from aoc import loader
from aoc.year_2023.day_04_scratchcards import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("Card 1: 1 | 2", 0),
        ("Card 1: 1 | 1", 1),
        ("Card 1: 1 2 | 1 2", 2),
        ("Card 1: 1 2 3 | 1 2 3", 4),
        (loader.get_module_data(solution, "fixture.txt"), 13),
        (loader.get_input_data(solution), 21821),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("Card 1: 1 | 2", 1),
        ("Card 1: 1 | 2\nCard 2: 1 | 2", 2),
        ("Card 1: 1 | 1\nCard 2: 1 | 2", 3),
        (loader.get_module_data(solution, "fixture.txt"), 30),
        (loader.get_input_data(solution), 5539496),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
