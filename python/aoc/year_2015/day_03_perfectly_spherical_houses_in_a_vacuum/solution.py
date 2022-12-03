import types

from aoc import solution

_DIRECTIONS = types.MappingProxyType(
    {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    },
)


class _Sled(object):
    def __init__(self) -> None:
        self._x_pos = 0
        self._y_pos = 0

    def move(self, direction: str) -> tuple[int, int]:
        match direction:
            case "<":
                self._x_pos -= 1
            case ">":
                self._x_pos += 1
            case "^":
                self._y_pos -= 1
            case "v":
                self._y_pos += 1

        return self._x_pos, self._y_pos


def _visit_houses(directions: str, sleds: int) -> int:
    grid = {(0, 0)}

    for starting_index in range(sleds):
        x_pos = 0
        y_pos = 0

        for direction in directions[starting_index::sleds]:
            match direction:
                case "<":
                    x_pos -= 1
                case ">":
                    x_pos += 1
                case "^":
                    y_pos -= 1
                case "v":
                    y_pos += 1

            grid.add((x_pos, y_pos))

    return len(grid)


class Solution(solution.Solution):
    day: int = 3
    year: int = 2015
    name: str = "Perfectly Spherical Houses in a Vacuum"

    def solve_part_one(self) -> int:
        return _visit_houses(self._input_data, 1)

    def solve_part_two(self) -> int:
        return _visit_houses(self._input_data, 2)
