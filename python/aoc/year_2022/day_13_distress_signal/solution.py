import functools
from collections.abc import Sequence
from typing import Any

import orjson

from aoc import solution


class Solution(solution.Solution):
    day: int = 13
    year: int = 2022
    name: str = "Distress Signal"

    def solve_part_one(self) -> int:
        correct_packets = []

        for index, pair in enumerate(self._input_data.split("\n\n"), start=1):
            first, second = pair.split("\n")

            if compare(orjson.loads(first), orjson.loads(second)) == -1:
                correct_packets.append(index)

        return sum(correct_packets)

    def solve_part_two(self) -> int:
        lines = [[[2]], [[6]]]

        for line in self._input_lines:
            if not line:
                continue

            lines.append(orjson.loads(line))

        sorted_lines = sorted(lines, key=functools.cmp_to_key(compare))

        return (sorted_lines.index([[2]]) + 1) * (sorted_lines.index([[6]]) + 1)


def compare(first: Sequence[Any], second: Sequence[Any]) -> int:
    for left, right in zip(first, second, strict=False):
        if isinstance(left, list) or isinstance(right, list):
            compared = compare(as_list(left), as_list(right))

            if compared == 0:
                continue

            return compared

        if left < right:
            return -1

        if left > right:
            return 1

    if len(first) < len(second):
        return -1

    if len(first) > len(second):
        return 1

    return 0


def as_list(maybe_list: Any) -> list[Any]:
    if isinstance(maybe_list, list):
        return maybe_list

    return [maybe_list]
