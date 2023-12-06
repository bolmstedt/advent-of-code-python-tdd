import pytest

from aoc import loader
from aoc.year_2023.day_05_if_you_give_a_seed_a_fertilizer import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("seeds: 1", 1),
        ("seeds: 1 2", 1),
        ("seeds: 1 2\nmap:\n3 1 1", 2),
        ("seeds: 1\nmap:\n3 1 1\n\nmap:\n7 3 1", 7),
        (loader.get_module_data(solution, "fixture.txt"), 35),
        (loader.get_input_data(solution), 462648396),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected
