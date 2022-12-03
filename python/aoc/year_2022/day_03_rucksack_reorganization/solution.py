import string

import more_itertools

from aoc import solution_helpers


class Solution(solution_helpers.Solution):
    day: int = 3
    year: int = 2022
    name: str = "Rucksack Reorganization"

    def _solve_part_one(self) -> int:
        return sum(
            string.ascii_letters.find(collision) + 1
            for rucksack in self._input_lines
            for collision in set.intersection(
                set(rucksack[: len(rucksack) // 2]),
                set(rucksack[len(rucksack) // 2 :]),
            )
        )

    def _solve_part_two(self) -> int:
        return sum(
            string.ascii_letters.find(collision) + 1
            for rucksacks in more_itertools.chunked(self._input_lines, 3)
            for collision in set.intersection(
                *[set(rucksack) for rucksack in rucksacks],
            )
        )
