import itertools
import string
from collections.abc import Iterable
from types import MappingProxyType

from aoc import solution

Cords = tuple[int, int]


class Heightmap(object):
    _heights = MappingProxyType(
        {
            "S": 1,
            "E": 26,
            **{
                letter: index
                for index, letter in enumerate(string.ascii_lowercase, start=1)
            },
        },
    )

    def __init__(self, input_lines: Iterable[str], *, fixed_start: bool = True):
        self.heightmap = {
            (x_pos, y_pos): self._heights[height]
            for y_pos, line in enumerate(input_lines)
            for x_pos, height in enumerate(line)
        }
        start_pos = (-1, -1)
        self.end_pos = (-1, -1)

        for row, line in enumerate(input_lines):
            start = line.find("S")
            end = line.find("E")

            if start != -1:
                start_pos = (start, row)

            if end != -1:
                self.end_pos = (end, row)

        self.visited = {start_pos}

        if not fixed_start:
            for pos, height in self.heightmap.items():
                if height == 1:
                    self.visited.add(pos)

    def walk(self) -> int:
        walks = list(self.visited)

        for current_round in itertools.count():
            new_walks = []

            for current_position in walks:
                for step in self._steps(current_position):
                    new_walks.append(step)
                    self.visited.add(step)

                    if step == self.end_pos:
                        return current_round + 1

            if not new_walks:
                break

            walks = new_walks

        return -1

    def _steps(self, pos: Cords) -> Iterable[Cords]:
        possible_steps = [
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1),
        ]

        for step in possible_steps:
            if step in self.visited:
                continue

            if step not in self.heightmap:
                continue

            if self.heightmap[pos] + 1 < self.heightmap[step]:
                continue

            yield step


class Solution(solution.Solution):
    day: int = 12
    year: int = 2022
    name: str = "Hill Climbing Algorithm"

    def solve_part_one(self) -> int:
        heightmap = Heightmap(self._input_lines)

        return heightmap.walk()

    def solve_part_two(self) -> int:
        heightmap = Heightmap(self._input_lines, fixed_start=False)

        return heightmap.walk()
