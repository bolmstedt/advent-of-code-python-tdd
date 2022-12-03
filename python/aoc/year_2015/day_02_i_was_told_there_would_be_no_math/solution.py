from typing import Iterable

from aoc import solution


def _calculate_box_area(length: int, width: int, height: int) -> int:
    return (
        2 * length * width
        + 2 * width * height
        + 2 * height * length
        + min(length * width, width * height, height * length)
    )


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
            _calculate_box_area(length, width, height)
            for length, width, height in self._process_data()
        )

    def solve_part_two(self) -> int:
        return sum(
            _calculate_ribbon_length(length, width, height)
            for length, width, height in self._process_data()
        )

    def _process_data(self) -> Iterable[tuple[int, int, int]]:
        yield from (
            _get_dimension_tuple(line) for line in self._input_data.splitlines()
        )
