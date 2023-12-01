from collections.abc import Callable, Iterator, Sequence

from aoc import solution


class Solution(solution.Solution):
    day: int = 4
    year: int = 2022
    name: str = "Camp Cleanup"

    def solve_part_one(self) -> int:
        return sum(self._process_range_pairs(_range_contains_another))

    def solve_part_two(self) -> int:
        return sum(self._process_range_pairs(_ranges_overlap))

    def _process_range_pairs(
        self,
        method: Callable[[Sequence[int], Sequence[int]], bool],
    ) -> Iterator[bool]:
        for pair in self._input_lines:
            sections = pair.split(",")
            ranges = []

            for section in sections:
                numbers = section.split("-")
                ranges.append(
                    (int(numbers[0]), int(numbers[1])),
                )

            yield method(ranges[0], ranges[1])


def _range_contains_another(first: Sequence[int], second: Sequence[int]) -> bool:
    return (
        first[0] <= second[0]
        and first[1] >= second[1]
        or second[0] <= first[0]
        and second[1] >= first[1]
    )


def _ranges_overlap(first: Sequence[int], second: Sequence[int]) -> bool:
    return first[0] <= second[1] and second[0] <= first[1]
