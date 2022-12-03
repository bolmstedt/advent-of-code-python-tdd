from aoc import solution


class NeverReachedCellarError(Exception):
    """Raised when Santa never reaches the basement."""


class Solution(solution.Solution):
    day: int = 1
    year: int = 2015
    name: str = "Not Quite Lisp"

    def solve_part_one(self) -> int:
        return self._input_data.count("(") - self._input_data.count(")")

    def solve_part_two(self) -> int:
        position = 0

        for iterator, stairs in enumerate(self._input_data, start=1):
            if stairs == "(":
                position += 1
            else:
                position -= 1

            if position < 0:
                return iterator

        raise NeverReachedCellarError()
