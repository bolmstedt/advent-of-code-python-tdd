import pytest

from aoc import loader
from aoc.year_2022.day_13_distress_signal import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("[1]\n[2]", 1),
        ("[2]\n[1]", 0),
        ("[1,1]\n[1,2]", 1),
        ("[1,2]\n[1,1]", 0),
        ("[[1]]\n[[1,1]]", 1),
        ("[[1,1]]\n[[1]]", 0),
        ("[[1,1]]\n[[2]]", 1),
        ("[[2]]\n[[1,1]]", 0),
        ("[1]\n[[2]]", 1),
        ("[2]\n[[1]]", 0),
        (loader.get_module_data(solution, "fixture.txt"), 13),
        (loader.get_input_data(solution), 5843),
    ],
)
def test_correct_orders(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 140),
        (loader.get_input_data(solution), 26289),
    ],
)
def test_sort(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
