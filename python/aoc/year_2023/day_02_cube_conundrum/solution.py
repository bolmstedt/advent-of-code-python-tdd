from typing import NamedTuple

from aoc import solution


class Round(NamedTuple):
    red: int = 0
    green: int = 0
    blue: int = 0


class Game(NamedTuple):
    identifier: int
    rounds: list[Round]


class Solution(solution.Solution):
    day: int = 2
    year: int = 2023
    name: str = "Cube Conundrum"

    def solve_part_one(self) -> int:
        return self._sum_of_ids(red=12, green=13, blue=14)

    def solve_part_two(self) -> int:
        powers = []

        for game in self._parse_games():
            minimal_count = Round()

            for _round in game.rounds:
                minimal_count = Round(
                    red=max(minimal_count.red, _round.red),
                    green=max(minimal_count.green, _round.green),
                    blue=max(minimal_count.blue, _round.blue),
                )

            powers.append(minimal_count.red * minimal_count.blue * minimal_count.green)

        return sum(powers)

    def _sum_of_ids(self, red: int, green: int, blue: int) -> int:
        valid_games = []

        for game in self._parse_games():
            if any(
                _round.red > red or _round.green > green or _round.blue > blue
                for _round in game.rounds
            ):
                continue

            valid_games.append(game.identifier)

        return sum(valid_games)

    def _parse_games(self) -> list[Game]:
        games = []

        for line in self._input_lines:
            game_part, rounds_part = line.split(":")
            games.append(
                Game(
                    identifier=int(game_part.split(" ")[1]),
                    rounds=_parse_rounds(rounds_part),
                ),
            )

        return games


def _parse_rounds(rounds_part: str) -> list[Round]:
    rounds = []
    raw_rounds = rounds_part.strip().split("; ")

    for raw_round in raw_rounds:
        counts = {}

        for raw_count in raw_round.strip().split(", "):
            count = raw_count.split(" ")
            counts[count[1]] = int(count[0])

        rounds.append(Round(**counts))

    return rounds
