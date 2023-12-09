import pytest

from aoc import loader
from aoc.year_2023.day_09_mirage_maintenance import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("0 0", 0),
        ("-1 0 1 2", 3),
        ("0 0 1 3 6", 10),
        ("15 10 6 3 1", 0),
        ("0 0 -1 -3 -6", -10),
        (loader.get_module_data(solution, "fixture.txt"), 114),
        (loader.get_input_data(solution), 2075724761),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("0 0", 0),
        ("0 1 2", -1),
        ("0 1 3 6", 0),
        ("10 6 3 1", 15),
        ("0 -1 -3 -6", 0),
        ("10 13 16 21 30 45", 5),
        pytest.param(loader.get_module_data(solution, "fixture.txt"), 2, id="fixture"),
        pytest.param(loader.get_input_data(solution), 1072, id="solution"),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
