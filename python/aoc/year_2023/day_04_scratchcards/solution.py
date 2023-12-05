import re
from typing import NamedTuple

from aoc import solution

_NUMBER_PATTERN = re.compile(r"(\d+)")


class Card(NamedTuple):
    matching_numbers: int


class Solution(solution.Solution):
    day: int = 4
    year: int = 2023
    name: str = "Scratchcards"

    def solve_part_one(self) -> int:
        return sum(2 ** (card - 1) for card in self._parse_cards() if card)

    def solve_part_two(self) -> int:
        cards = self._parse_cards()
        card_counts = [1 for _ in cards]

        for index, card in enumerate(cards):
            for _ in range(card_counts[index]):
                for wins in range(card):
                    card_counts[index + wins + 1] += 1

        return sum(card_counts)

    def _parse_cards(self) -> list[int]:
        cards = []

        for line in self._input_lines:
            winning, numbers = line.split(":")[1].split("|")
            cards.append(
                len(
                    {int(match) for match in _NUMBER_PATTERN.findall(winning)}
                    & {int(match) for match in _NUMBER_PATTERN.findall(numbers)},
                ),
            )

        return cards
