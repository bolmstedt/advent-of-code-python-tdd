from aoc import solution

_PART_ONE_WINDOW = 4
_PART_TWO_WINDOW = 14


class Solution(solution.Solution):
    day: int = 6
    year: int = 2022
    name: str = "Tuning Trouble"

    def solve_part_one(self) -> int:
        return self._find_unique_window(_PART_ONE_WINDOW)

    def solve_part_two(self) -> int:
        return self._find_unique_window(_PART_TWO_WINDOW)

    def _find_unique_window(self, length: int) -> int:
        max_length = len(self._input_data)
        index = length - 1

        while index <= max_length:
            for current in range(length):
                matched = self._input_data[index - length + 1 : index - current].rfind(
                    self._input_data[index - current],
                )

                if matched > -1:
                    index += matched + 1
                    break
            else:
                return index + 1

        return 0
