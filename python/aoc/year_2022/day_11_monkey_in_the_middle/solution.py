import math
import operator
from typing import Any

from aoc import solution


class Solution(solution.Solution):
    day: int = 11
    year: int = 2022
    name: str = "Monkey in the Middle"

    def solve_part_one(self) -> int:
        return self._calculate_monkey_business(20)

    def solve_part_two(self) -> int:
        return self._calculate_monkey_business(10000, relief=False)

    def _calculate_monkey_business(self, rounds: int, *, relief: bool = True) -> int:
        monkeys = self._parse_monkeys()
        lowest_common = math.prod([monkey["div"] for monkey in monkeys])

        business = [0 for _ in range(len(monkeys))]

        for _current_round in range(rounds):
            for index, monkey in enumerate(monkeys):
                while monkey["items"]:
                    business[index] += 1
                    worry = monkey["modifier"](monkey["items"].pop(0), monkey["amount"])

                    if relief:
                        worry //= 3
                    else:
                        worry %= lowest_common

                    target = (
                        monkey["false"] if worry % monkey["div"] else monkey["true"]
                    )
                    monkeys[target]["items"].append(worry)

        business.sort()

        return business.pop() * business.pop()

    def _parse_monkeys(self) -> list[dict[str, Any]]:
        monkeys = []
        raw_monkeys = self._input_data.split("\n\n")

        for raw_monkey in raw_monkeys:
            lines = raw_monkey.splitlines()

            if lines[2][25:] == "old":
                modifier = operator.pow
            else:
                modifier = operator.add if lines[2][23] == "+" else operator.mul

            monkeys.append(
                {
                    "items": list(map(int, lines[1][18:].split(", "))),
                    "modifier": modifier,
                    "amount": 2 if lines[2][25:] == "old" else int(lines[2][25:]),
                    "div": int(lines[3][21:]),
                    "true": int(lines[4][-1]),
                    "false": int(lines[5][-1]),
                },
            )

        return monkeys
