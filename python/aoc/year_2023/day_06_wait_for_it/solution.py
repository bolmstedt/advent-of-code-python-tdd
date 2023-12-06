import math
import re
from typing import NamedTuple

from aoc import solution

_NUMBER_PATTERN = re.compile(r"(\d+)")


class Race(NamedTuple):
    limit: int
    distance: int


class Solution(solution.Solution):
    day: int = 6
    year: int = 2023
    name: str = "Wait For It"

    def solve_part_one(self) -> int:
        return math.prod(ways_to_win(race) for race in self._parse_races())

    def solve_part_two(self) -> int:
        return ways_to_win(self._parse_long_race())

    def _parse_races(self) -> list[Race]:
        limits = _NUMBER_PATTERN.findall(self._input_lines[0])
        distances = _NUMBER_PATTERN.findall(self._input_lines[1])

        return [
            Race(
                limit=int(limit),
                distance=int(distance),
            )
            for limit, distance in zip(limits, distances, strict=True)
        ]

    def _parse_long_race(self) -> Race:
        limits = _NUMBER_PATTERN.findall(self._input_lines[0])
        distances = _NUMBER_PATTERN.findall(self._input_lines[1])

        return Race(
            limit=int("".join(limits)),
            distance=int("".join(distances)),
        )


def ways_to_win(race: Race) -> int:
    wins = 0
    minimum_charge = math.ceil(race.distance / race.limit)
    maximum_charge = race.limit - minimum_charge + 1

    for charge in range(minimum_charge, maximum_charge):
        if charge * (race.limit - charge) > race.distance:
            wins += 1

    return wins
