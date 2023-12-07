from collections import Counter
from collections.abc import Mapping
from types import MappingProxyType
from typing import NamedTuple

from aoc import solution

_BASE = 13
_TYPE_MULTIPLIER = _BASE**5

_CARDS_PART_ONE: Mapping[str, int] = MappingProxyType(
    {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
    },
)


_CARDS_PART_TWO: Mapping[str, int] = MappingProxyType(
    {
        "A": 13,
        "K": 12,
        "Q": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2,
        "J": 1,
    },
)

_HANDS = {
    (5,): 6,
    (4, 1): 5,
    (3, 2): 4,
    (3, 1): 3,
    (2, 2): 2,
    (2, 1): 1,
    (1, 1): 0,
}


class Hand(NamedTuple):
    bid: int
    cards: tuple[int, int, int, int, int]


class Solution(solution.Solution):
    day: int = 7
    year: int = 2023
    name: str = "Camel Cards"

    def solve_part_one(self) -> int:
        return sum(
            hand.bid * score
            for score, hand in enumerate(
                sorted(self._parse_hands(_CARDS_PART_ONE), key=_hand_score),
                1,
            )
        )

    def solve_part_two(self) -> int:
        return sum(
            hand.bid * score
            for score, hand in enumerate(
                sorted(self._parse_hands(_CARDS_PART_TWO), key=_hand_joker_score),
                1,
            )
        )

    def _parse_hands(self, mapping: Mapping[str, int]) -> list[Hand]:
        return [
            Hand(
                bid=int(line[6:]),
                cards=(
                    mapping[line[0]],
                    mapping[line[1]],
                    mapping[line[2]],
                    mapping[line[3]],
                    mapping[line[4]],
                ),
            )
            for line in self._input_lines
        ]


def _hand_score(hand: Hand) -> int:
    return _card_score(hand) + _hand_type_score(Counter(hand.cards)) * _TYPE_MULTIPLIER


def _hand_joker_score(hand: Hand) -> int:
    return _card_score(hand) + _hand_type_score(_joker_hand(hand)) * _TYPE_MULTIPLIER


def _card_score(hand: Hand) -> int:
    return sum(
        card * _BASE**value
        for card, value in zip(hand.cards, range(4, -1, -1), strict=True)
    )


def _hand_type_score(hand: Counter[int]) -> int:
    if len(hand) == 1:
        return 6

    significant = hand.most_common(2)

    return _HANDS[(significant[0][1], significant[1][1])]


def _joker_hand(hand: Hand) -> Counter[int]:
    counter = Counter(hand.cards)

    if 1 in counter and len(counter) > 1:
        jokers = counter.pop(1)
        most_common = counter.most_common(1)
        counter.update(most_common[0][0] for _ in range(jokers))

    return counter
