import itertools
from typing import Iterable, Sequence

from aoc import solution

Coordinate = tuple[int, int]


class Cave(object):
    def __init__(self, input_lines: Iterable[str], add_floor: bool = False):
        self.start = (500, 0)
        self.cave = {self.start}

        self._fill_cave(input_lines)

        self.max_depth = max(point[1] for point in self.cave)
        self.has_floor = add_floor

        if self.has_floor:
            self.max_depth = self.max_depth + 2
            floor_range = range(
                self.start[0] - self.max_depth,
                self.start[0] + self.max_depth + 1,
            )

            for floor_x in floor_range:
                self.cave.add((floor_x, self.max_depth))

    def enter_sandman(self) -> int:
        for index in itertools.count():
            current = self.start
            new = self._next_move(current)

            if new is None:
                return index + 1

            while new is not None:
                current = new
                new = self._next_move(current)

                if new and new[1] > self.max_depth:
                    return index

            self.cave.add(current)

        return -1

    def _next_move(self, sand: Coordinate) -> Coordinate | None:
        possible_moves = [
            (sand[0], sand[1] + 1),
            (sand[0] - 1, sand[1] + 1),
            (sand[0] + 1, sand[1] + 1),
        ]

        for possible_move in possible_moves:
            if possible_move not in self.cave:
                return possible_move

    def _fill_cave(self, input_lines: Iterable[str]) -> None:
        for line in input_lines:
            for origin, destination in itertools.pairwise(line.split(" -> ")):
                self._fill_coordinates(origin.split(","), destination.split(","))

    def _fill_coordinates(
        self,
        org_cords: Sequence[str],
        dest_cords: Sequence[str],
    ) -> None:
        y_coords = sorted([int(org_cords[1]), int(dest_cords[1])])
        x_coords = sorted([int(org_cords[0]), int(dest_cords[0])])

        for y_coord in range(y_coords[0], y_coords[1] + 1):
            self.cave.add((x_coords[0], y_coord))

        for x_coord in range(x_coords[0], x_coords[1] + 1):
            self.cave.add((x_coord, y_coords[0]))


class Solution(solution.Solution):
    day: int = 14
    year: int = 2022
    name: str = "Regolith Reservoir"

    def solve_part_one(self) -> int:
        cave = Cave(self._input_lines)

        return cave.enter_sandman()

    def solve_part_two(self) -> int:
        cave = Cave(self._input_lines, add_floor=True)

        return cave.enter_sandman()
