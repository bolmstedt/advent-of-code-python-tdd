import copy
import math
import operator
from collections.abc import Callable
from typing import Any, NamedTuple

from aoc import solution


class Monkey(NamedTuple):
    items: list[int]
    modifier: Callable[[Any, Any], Any]
    amount: int
    div: int
    true: int
    false: int


class Solution(solution.Solution):
    day: int = 11
    year: int = 2022
    name: str = "Monkey in the Middle"

    def solve_part_one(self) -> int:
        return self._calculate_simple_monkey_business(20)

    def solve_part_two(self) -> int:
        return self._calculate_more_monkey_business(10000)

    def _calculate_simple_monkey_business(self, rounds: int) -> int:
        monkeys = self._parse_monkeys()

        business = [0 for _ in range(len(monkeys))]

        for _current_round in range(rounds):
            for index, monkey in enumerate(monkeys):
                business[index] += len(monkey.items)

                items_to_give = (
                    monkey.modifier(item, monkey.amount) // 3 for item in monkey.items
                )

                for item in items_to_give:
                    monkeys[
                        monkey.false if item % monkey.div else monkey.true
                    ].items.append(
                        item,
                    )

                monkey.items.clear()

        business.sort()

        return business.pop() * business.pop()

    def _calculate_more_monkey_business(self, rounds: int) -> int:
        monkeys = self._parse_monkeys()
        lcm = math.lcm(*(monkey.div for monkey in monkeys))

        business = [0 for _ in range(len(monkeys))]
        distinct_rounds: list[list[int]] = []
        distinct_cycle: list[list[int]] = []
        current_round = 0

        for _ in range(rounds):
            previous_business = copy.copy(business)

            for index, monkey in enumerate(monkeys):
                business[index] += len(monkey.items)

                items_to_give = (
                    monkey.modifier(item, monkey.amount) % lcm for item in monkey.items
                )

                for item in items_to_give:
                    monkeys[
                        monkey.false if item % monkey.div else monkey.true
                    ].items.append(item)

                monkey.items.clear()

            distinct_round = [
                prev - current
                for prev, current in zip(business, previous_business, strict=True)
            ]

            current_round += 1

            if len(distinct_rounds) > 5 and distinct_round in distinct_rounds:
                if distinct_cycle == distinct_rounds:
                    distinct_cycle.append(distinct_cycle.pop(0))
                    break

                distinct_cycle = copy.deepcopy(distinct_rounds)
                distinct_rounds.clear()

            distinct_rounds.append(distinct_round)

        cycle_length = len(distinct_cycle)
        cycle_sum = [sum(monkey) for monkey in zip(*distinct_cycle, strict=True)]

        remaining_rounds = rounds - current_round
        remaining_cycles = remaining_rounds // cycle_length
        remaining_rounds -= cycle_length * remaining_cycles

        for index, _ in enumerate(monkeys):
            business[index] += cycle_sum[index] * remaining_cycles

        for remaining_round in distinct_cycle[:remaining_rounds]:
            for index, _ in enumerate(monkeys):
                business[index] += remaining_round[index]

        business.sort()

        return business.pop() * business.pop()

    def _parse_monkeys(self) -> list[Monkey]:
        monkeys = []
        raw_monkeys = self._input_data.split("\n\n")

        for raw_monkey in raw_monkeys:
            lines = raw_monkey.splitlines()

            if lines[2][25:] == "old":
                modifier = operator.pow
            else:
                modifier = operator.add if lines[2][23] == "+" else operator.mul

            monkeys.append(
                Monkey(
                    items=list(map(int, lines[1][18:].split(", "))),
                    modifier=modifier,
                    amount=2 if lines[2][25:] == "old" else int(lines[2][25:]),
                    div=int(lines[3][21:]),
                    true=int(lines[4][-1]),
                    false=int(lines[5][-1]),
                ),
            )

        return monkeys
