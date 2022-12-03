import string

import more_itertools

from aoc import solution


class Solution(solution.Solution):
    day: int = 3
    year: int = 2022
    name: str = "Rucksack Reorganization"

    _priorities = {
        letter: priority
        for priority, letter in enumerate(string.ascii_letters, start=1)
    }

    def solve_part_one(self) -> int:
        return sum(
            self._priorities[
                more_itertools.first(
                    set.intersection(
                        set(rucksack[: len(rucksack) // 2]),
                        set(rucksack[len(rucksack) // 2 :]),
                    ),
                )
            ]
            for rucksack in self._input_lines
        )

    def solve_part_two(self) -> int:
        return sum(
            self._priorities[
                more_itertools.first(
                    set.intersection(
                        *[set(rucksack) for rucksack in rucksacks],
                    ),
                )
            ]
            for rucksacks in more_itertools.chunked(self._input_lines, 3)
        )
