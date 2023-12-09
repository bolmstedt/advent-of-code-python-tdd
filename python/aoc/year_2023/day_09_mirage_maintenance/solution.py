import itertools
from collections.abc import Sequence

from aoc import solution


class Solution(solution.Solution):
    day: int = 9
    year: int = 2023
    name: str = "Mirage Maintenance"

    def solve_part_one(self) -> int:
        return sum(_predict_next_value(history) for history in self._parse_history())

    def solve_part_two(self) -> int:
        return sum(
            _predict_previous_value(history) for history in self._parse_history()
        )

    def _parse_history(self) -> list[list[int]]:
        return [
            list(map(int, (number for number in line.split(" "))))
            for line in self._input_lines
        ]


def _predict_next_value(history: Sequence[int]) -> int:
    last_numbers = []

    while len(set(history)) > 1:
        last_numbers.append(history[-1])
        history = [second - first for first, second in itertools.pairwise(history)]

    last_numbers.append(history[-1])

    return sum(last_numbers)


def _predict_previous_value(history: Sequence[int]) -> int:
    first_numbers = []

    while len(set(history)) > 1:
        first_numbers.append(history[0])
        history = [second - first for first, second in itertools.pairwise(history)]

    first_numbers.append(history[0])
    difference = 0

    for number in first_numbers[::-1]:
        difference = number - difference

    return difference
