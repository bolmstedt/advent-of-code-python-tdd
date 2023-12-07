import math
import re
from typing import NamedTuple

from aoc import solution

_NUMBER_PATTERN = re.compile(r"(\d+)")


class Race(NamedTuple):
    limit: int
    record: int


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
        records = _NUMBER_PATTERN.findall(self._input_lines[1])

        return [
            Race(
                limit=int(limit),
                record=int(record),
            )
            for limit, record in zip(limits, records, strict=True)
        ]

    def _parse_long_race(self) -> Race:
        limits = _NUMBER_PATTERN.findall(self._input_lines[0])
        records = _NUMBER_PATTERN.findall(self._input_lines[1])

        return Race(
            limit=int("".join(limits)),
            record=int("".join(records)),
        )


def ways_to_win(race: Race) -> int:
    minimum_charge = math.ceil(
        (race.limit - math.sqrt(race.limit**2 - 4 * race.record + 1)) / 2,
    )

    while race.limit * minimum_charge - minimum_charge**2 <= race.record:
        minimum_charge += 1

    return race.limit - minimum_charge * 2 + 1
