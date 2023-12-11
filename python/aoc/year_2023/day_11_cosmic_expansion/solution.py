import itertools
from collections.abc import Sequence
from typing import TypeAlias

from aoc import solution

_Coordinates: TypeAlias = tuple[int, int]


class Solution(solution.Solution):
    day: int = 11
    year: int = 2023
    name: str = "Cosmic Expansion"

    def solve_part_one(self) -> int:
        return self.distance_between_galaxies(2)

    def solve_part_two(self) -> int:
        return self.distance_between_galaxies(1000000)

    def distance_between_galaxies(self, expansion_factor: int) -> int:
        rows, columns = self._rows_and_columns_without_galaxies()

        return sum(
            _manhattan_distance(first, second)
            + _expansion(first, second, rows, columns, expansion_factor - 1)
            for first, second in itertools.combinations(self._parse_galaxies(), 2)
        )

    def _parse_galaxies(self) -> set[_Coordinates]:
        galaxies = set()

        for y_pos, line in enumerate(self._input_lines):
            for x_pos, location in enumerate(line):
                if location == "#":
                    galaxies.add((x_pos, y_pos))

        return galaxies

    def _rows_and_columns_without_galaxies(self) -> tuple[set[int], set[int]]:
        rows = _rows_without_galaxies(self._input_lines)
        columns = _rows_without_galaxies(_rotate_map(self._input_lines))

        return rows, columns


def _expansion(
    first: _Coordinates,
    second: _Coordinates,
    rows: set[int],
    columns: set[int],
    expansion_factor: int,
) -> int:
    col_span = min(first[0], second[0]), max(first[0], second[0])
    row_span = min(first[1], second[1]), max(first[1], second[1])
    col_span_set = set(range(col_span[0] + 1, col_span[1]))
    row_span_set = set(range(row_span[0] + 1, row_span[1]))
    rows_without_galaxies = rows.intersection(row_span_set)
    columns_without_galaxies = columns.intersection(col_span_set)

    return (
        len(rows_without_galaxies) * expansion_factor
        + len(columns_without_galaxies) * expansion_factor
    )


def _rows_without_galaxies(galaxy_map: Sequence[str]) -> set[int]:
    return {x_pos for x_pos, line in enumerate(galaxy_map) if "#" not in line}


def _rotate_map(map_: Sequence[str]) -> list[str]:
    return ["".join(list(position)[::-1]) for position in zip(*map_, strict=True)]


def _manhattan_distance(origin: _Coordinates, destination: _Coordinates) -> int:
    return abs(origin[0] - destination[0]) + abs(origin[1] - destination[1])
