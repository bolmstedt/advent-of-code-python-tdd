import pytest

from aoc import loader
from aoc.year_2023.day_07_camel_cards import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("22222 1", 1),
        ("22222 2\n33333 1", 4),
        ("33333 1\n22222 2", 4),
        ("AAAAA 1\nTTTTT 2", 4),
        ("33333 1\n33332 2", 4),
        ("33332 1\n33322 2", 4),
        ("33322 1\n44432 2", 4),
        ("44432 1\n44332 2", 4),
        ("44332 1\n55432 2", 4),
        ("55432 1\n65432 2", 4),
        pytest.param(
            loader.get_module_data(solution, "fixture.txt"),
            6440,
            id="fixture",
        ),
        pytest.param(loader.get_input_data(solution), 248217452, id="solution"),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("33JJJ 1\n33332 2", 4),
        ("22222 1\nJJJJ3 2", 4),
        ("22222 1\nJJJJJ 2", 4),
        ("JJJJ3 1\nJJJJJ 2", 4),
        pytest.param(
            loader.get_module_data(solution, "fixture.txt"),
            5905,
            id="fixture",
        ),
        pytest.param(loader.get_input_data(solution), 245576185, id="solution"),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
