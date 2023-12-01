from collections.abc import Iterator, Sequence

import more_itertools

from aoc import solution

_Stacks = dict[int, list[str]]
_Operations = tuple[int, int, int]


class Solution(solution.Solution):
    day: int = 5
    year: int = 2022
    name: str = "Supply Stacks"

    def solve_part_one(self) -> str:
        stacks, operations = self._process_input()

        for operation in operations:
            for _ in range(operation[0]):
                stacks[operation[2]].insert(
                    0,
                    stacks[operation[1]].pop(0),
                )

        return "".join(more_itertools.first(stack) for stack in stacks.values())

    def solve_part_two(self) -> str:
        stacks, operations = self._process_input()

        for operation in operations:
            popped = [stacks[operation[1]].pop(0) for _ in range(operation[0])]

            popped.reverse()

            for crate in popped:
                stacks[operation[2]].insert(0, crate)

        return "".join(more_itertools.first(stack) for stack in stacks.values())

    def _process_input(self) -> tuple[_Stacks, Iterator[_Operations]]:
        stacks, operations = self._input_data.split("\n\n")

        return _process_stacks(stacks.splitlines()), _process_operations(operations)


def _process_stacks(stacks_lines: Sequence[str]) -> _Stacks:
    stacks: _Stacks = {}

    for index in stacks_lines[-1][1::4]:
        stacks[int(index)] = []

    for line in stacks_lines[:-1]:
        for stack, crate in enumerate(line[1::4], start=1):
            if crate.strip():
                stacks[stack].append(crate)

    return stacks


def _process_operations(operations_raw: str) -> Iterator[_Operations]:
    for operation in operations_raw.splitlines():
        parts = operation.split(" from ")

        yield (
            int(parts[0][5:]),
            int(parts[1][0]),
            int(parts[1][-1]),
        )
