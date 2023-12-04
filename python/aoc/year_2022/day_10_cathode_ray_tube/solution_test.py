import pytest

from aoc import loader
from aoc.year_2022.day_10_cathode_ray_tube import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("noop\n" * 220, 720),
        (loader.get_module_data(solution, "fixture.txt"), 13140),
        (loader.get_input_data(solution), 15880),
    ],
)
def test_value_of_register(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


_EXPECTED_FIXTURE_OUTPUT = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

_EXPECTED_SOLUTION_OUTPUT = """
###..#.....##..####.#..#..##..####..##..
#..#.#....#..#.#....#.#..#..#....#.#..#.
#..#.#....#....###..##...#..#...#..#....
###..#....#.##.#....#.#..####..#...#.##.
#....#....#..#.#....#.#..#..#.#....#..#.
#....####..###.#....#..#.#..#.####..###.
"""


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), _EXPECTED_FIXTURE_OUTPUT),
        (loader.get_input_data(solution), _EXPECTED_SOLUTION_OUTPUT),
    ],
)
def test_long_rope(input_data: str, expected: str) -> None:
    assert solution.Solution(input_data).solve_part_two().strip() == expected.strip()
