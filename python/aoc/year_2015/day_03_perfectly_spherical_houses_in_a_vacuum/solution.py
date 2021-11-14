import types

from aoc import solution_helpers

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

    @property
    def coordinates(self) -> str:
        return "{x},{y}".format(x=self._x_pos, y=self._y_pos)

    def move(self, direction: str) -> str:
        x_change, y_change = _DIRECTIONS[direction]
        self._x_pos += x_change
        self._y_pos += y_change

        return self.coordinates


def _visit_houses(directions: str, sleds: list[_Sled]) -> int:
    grid = {sleds[0].coordinates}
    number_of_sleds = len(sleds)

    for index, sled in enumerate(sleds):
        for direction in directions[index::number_of_sleds]:
            grid.add(sled.move(direction))

    return len(grid)


class Solution(solution_helpers.Solution):
    day: int = 3
    year: int = 2015
    name: str = "Perfectly Spherical Houses in a Vacuum"

    def _solve_part_one(self) -> int:
        return _visit_houses(self._input_data, [_Sled()])

    def _solve_part_two(self) -> int:
        return _visit_houses(self._input_data, [_Sled(), _Sled()])
