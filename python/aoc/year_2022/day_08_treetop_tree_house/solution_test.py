import pytest

from aoc import loader
from aoc.year_2022.day_08_treetop_tree_house import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("00\n00", 4),
        ("000\n000\n000", 8),
        ("000\n010\n000", 9),
        ("101\n111\n111", 9),
        ("111\n110\n111", 9),
        ("111\n111\n101", 9),
        ("111\n011\n111", 9),
        (loader.get_module_data(solution, "fixture.txt"), 21),
        (loader.get_input_data(solution), 1736),
    ],
)
def test_trees_visible_from_edge(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("00\n00", 0),
        ("000\n000\n000", 1),
        ("00100\n00000\n10101\n00000\n00100", 16),
        ("00000\n00000\n10101\n00000\n00100", 16),
        ("00100\n00000\n10100\n00000\n00100", 16),
        ("00100\n00000\n10101\n00000\n00000", 16),
        ("00100\n00000\n00101\n00000\n00100", 16),
        ("000\n010\n000", 1),
        (loader.get_module_data(solution, "fixture.txt"), 8),
        (loader.get_input_data(solution), 268800),
    ],
)
def test_scenic_score(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
