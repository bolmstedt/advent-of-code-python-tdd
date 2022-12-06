import itertools

import more_itertools

from aoc import solution

_PART_ONE_WINDOW = 4
_PART_TWO_WINDOW = 14


class Solution(solution.Solution):
    day: int = 6
    year: int = 2022
    name: str = "Tuning Trouble"

    def solve_part_one(self) -> int:
        return self._find_small_unique_window(_PART_ONE_WINDOW)

    def solve_part_two(self) -> int:
        return self._find_large_unique_window(_PART_TWO_WINDOW)

    def _find_small_unique_window(self, length: int) -> int:
        windows = enumerate(more_itertools.windowed(self._input_data, length), length)

        for index, window in windows:
            if len(set(window)) == length:
                return index

        return 0

    def _find_large_unique_window(self, length: int) -> int:
        windows = enumerate(more_itertools.windowed(self._input_data, length), length)
        index, window = next(windows)
        missing_unique_length = length - len(set(window))

        while missing_unique_length:
            index, window = next(
                itertools.islice(
                    windows,
                    missing_unique_length - 1,
                    missing_unique_length,
                ),
            )
            missing_unique_length = length - len(set(window))

        return index
