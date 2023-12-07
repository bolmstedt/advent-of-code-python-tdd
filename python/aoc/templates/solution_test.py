import pytest

from aoc import loader
from aoc.year_2222.__NAME__ import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("foo", 0),
        # (loader.get_module_data(solution, "fixture.txt"), 0),
        # (loader.get_input_data(solution), 0),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


# @pytest.mark.parametrize(
#     ("input_data", "expected"),
#     [
#         ("foo", 0),
#         # (loader.get_module_data(solution, "fixture.txt"), 0),
#         # (loader.get_input_data(solution), 0),
#     ],
# )
# def test_part_two(input_data: str, expected: int) -> None:
#     assert solution.Solution(input_data).solve_part_two() == expected
