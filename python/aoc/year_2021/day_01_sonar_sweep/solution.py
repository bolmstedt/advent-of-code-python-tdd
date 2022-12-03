import itertools
from typing import Iterable, cast

import more_itertools

from aoc import solution_helpers


class Solution(solution_helpers.Solution):
    day: int = 1
    year: int = 2021
    name: str = "Sonar Sweep"

    def _solve_part_one(self) -> int:
        return sum(
            int(current > previous)
            for previous, current in itertools.pairwise(map(int, self._input_lines))
        )

    def _solve_part_two(self) -> int:
        input_lines = filter(None, self._input_data.splitlines())
        input_parsed = map(int, input_lines)
        summed_windows = [
            sum(cast(Iterable[int], window))
            for window in more_itertools.windowed(input_parsed, 3)
        ]

        return sum(
            current > previous
            for previous, current in itertools.pairwise(summed_windows)
        )
