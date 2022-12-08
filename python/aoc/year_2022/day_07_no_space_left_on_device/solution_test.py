import pytest

from aoc import loader
from aoc.year_2022.day_07_no_space_left_on_device import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("$ cd /\n$ ls\n1 a", 1),
        ("$ cd /\n$ ls\ndir foo\n1 a\n2 b", 3),
        ("$ cd /\n$ ls\n1 a\n2 b\n$ cd foo\n$ ls\n100001 c", 0),
        (loader.get_module_data(solution, "fixture.txt"), 95437),
        (loader.get_input_data(solution), 1908462),
    ],
)
def test_total_directory_size(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("$ cd /\n$ ls\n45000000 a", 45000000),
        (loader.get_module_data(solution, "fixture.txt"), 24933642),
        (loader.get_input_data(solution), 3979145),
    ],
)
def test_smallest_directory_to_delete(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
