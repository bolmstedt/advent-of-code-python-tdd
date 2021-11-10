import abc
from typing import Union

import typer


class SolutionResult(object):
    def __init__(self, solution_result: Union[str, int]):
        self._solution_result = solution_result

    def __str__(self) -> str:
        return str(self._solution_result)

    def __repr__(self) -> str:
        return str(self._solution_result)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (str, int)):
            return False

        return str(self._solution_result) == str(other)


class Solution(abc.ABC):
    day: int
    year: int
    name: str

    def __init__(self, input_data: str):
        self._input_data = input_data

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

    def solve_part_one(self) -> SolutionResult:
        return SolutionResult(self._solve_part_one())

    def solve_part_two(self) -> SolutionResult:
        return SolutionResult(self._solve_part_two())

    @abc.abstractmethod
    def _solve_part_one(self) -> Union[str, int]:
        """Implement part one's solution."""

    @abc.abstractmethod
    def _solve_part_two(self) -> Union[str, int]:
        """Implement part two's solution."""


class Solver(object):
    def __init__(self, solution: Solution):
        self._solution = solution

    def solve(self) -> None:
        typer.echo("Solving {name}".format(name=self._solution.solution_name))
        solution_result = self._solution.solve_part_one()
        typer.echo("- Part One: {result}".format(result=solution_result))
        solution_result = self._solution.solve_part_two()
        typer.echo("- Part Two: {result}".format(result=solution_result))
