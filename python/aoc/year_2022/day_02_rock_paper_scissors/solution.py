from __future__ import annotations

from types import MappingProxyType

from aoc import solution_helpers

_MOVES = MappingProxyType(
    {
        "A": 0,
        "B": 1,
        "C": 2,
        "X": 0,
        "Y": 1,
        "Z": 2,
    },
)
_PART_ONE_POINTS = (
    "B X",
    "C Y",
    "A Z",
    "A X",
    "B Y",
    "C Z",
    "C X",
    "A Y",
    "B Z",
)
_PART_TWO_POINTS = (
    "B X",
    "C X",
    "A X",
    "A Y",
    "B Y",
    "C Y",
    "C Z",
    "A Z",
    "B Z",
)


class Solution(solution_helpers.Solution):
    day: int = 2
    year: int = 2022
    name: str = "Rock Paper Scissors"

    def _solve_part_one(self) -> int:
        return sum(
            self._input_data.count(game) * points
            for points, game in enumerate(_PART_ONE_POINTS, start=1)
        )

    def _solve_part_two(self) -> int:
        return sum(
            self._input_data.count(game) * points
            for points, game in enumerate(_PART_TWO_POINTS, start=1)
        )

    def _math_solve_part_one(self) -> int:
        return sum(
            _calculate_points(_MOVES[game_round[0]], _MOVES[game_round[2]])
            for game_round in self._input_lines
        )

    def _math_solve_part_two(self) -> int:
        return sum(
            _calculate_decided_points(_MOVES[game_round[0]], _MOVES[game_round[2]])
            for game_round in self._input_lines
        )


def _calculate_points(opponent: int, player: int) -> int:
    return player + 1 + (player - opponent + 1) % 3 * 3


def _calculate_decided_points(opponent: int, player: int) -> int:
    return _calculate_points(
        opponent,
        _get_player_move(
            player,
            opponent,
        ),
    )


def _get_player_move(opponent: int, player: int) -> int:
    return (player + opponent - 1) % 3
