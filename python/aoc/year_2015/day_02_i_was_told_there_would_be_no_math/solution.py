from collections.abc import Iterable
from itertools import starmap

from aoc import solution


def _calculate_box_area(length: int, width: int, height: int) -> int:
    lw = length * width
    wh = width * height
    hl = height * length

    return 2 * (lw + wh + hl) + min(lw, wh, hl)


def _get_dimension_tuple(dimensions: str) -> tuple[int, int, int]:
    dimensions_list = sorted(map(int, dimensions.split("x")))

    return dimensions_list[0], dimensions_list[1], dimensions_list[2]


def _calculate_ribbon_length(length: int, width: int, height: int) -> int:
    return 2 * (length + width) + length * width * height


class Solution(solution.Solution):
    day: int = 2
    year: int = 2015
    name: str = "I Was Told There Would Be No Math"

    def solve_part_one(self) -> int:
        return sum(
            starmap(_calculate_box_area, self._process_data()),
        )

    def solve_part_two(self) -> int:
        return sum(
            starmap(_calculate_ribbon_length, self._process_data()),
        )

    def _process_data(self) -> Iterable[tuple[int, int, int]]:
        yield from (
            _get_dimension_tuple(line) for line in self._input_data.splitlines()
        )
