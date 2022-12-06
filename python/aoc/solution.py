import abc


class Solution(abc.ABC):
    day: int
    year: int
    name: str

    def __init__(self, input_data: str):
        self._input_data = input_data.rstrip("\n")
        self._input_lines = self._input_data.splitlines()

    @property
    def module(self) -> str:
        return self.__module__

    @property
    def solution_name(self) -> str:
        return "{year}:{day} - {name}".format(
            year=self.year,
            day=self.day,
            name=self.name,
        )

    @abc.abstractmethod
    def solve_part_one(self) -> int | str:
        """Implement part one's solution."""

    @abc.abstractmethod
    def solve_part_two(self) -> int | str:
        """Implement part two's solution."""
