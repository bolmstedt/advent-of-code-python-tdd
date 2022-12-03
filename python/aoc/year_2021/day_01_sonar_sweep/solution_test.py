import pytest

from aoc import loader
from aoc.year_2021.day_01_sonar_sweep import solution


@pytest.mark.parametrize(
    ("test_data", "expected"),
    [
        ("1\n", 0),
        ("1\n2", 1),
        ("1\n2\n3", 2),
        ("1\n2\n1\n0", 1),
        (loader.get_module_data(solution, "fixture.txt"), 7),
        (loader.get_input_data(solution), 1713),
    ],
)
def test_depth_increases_number_of_times(test_data: str, expected: int) -> None:
    assert solution.Solution(test_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("test_data", "expected"),
    [
        ("1\n1\n1", 0),
        ("1\n1\n1\n1", 0),
        ("1\n1\n1\n2", 1),
        ("1\n1\n1\n2\n1", 1),
        ("1\n1\n1\n2\n1\n3", 2),
        (loader.get_module_data(solution, "fixture.txt"), 5),
    ],
)
def test_depth_increases_for_sliding_window(test_data: str, expected: int) -> None:
    assert solution.Solution(test_data).solve_part_two() == expected
