import math
import time
from typing import Callable

import typer

from aoc import solution


class SolutionResult(object):
    def __init__(self, solution_result: int | str):
        self._solution_result = solution_result

    def __str__(self) -> str:
        return str(self._solution_result)

    def __repr__(self) -> str:
        return str(self._solution_result)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (str, int)):
            return False

        return str(self._solution_result) == str(other)


class Solver(object):
    def __init__(self, day_solution: solution.Solution):
        self._solution = day_solution

    def solve(self) -> None:
        typer.echo("Solving {name}".format(name=self._solution.solution_name))
        solution_result = SolutionResult(self._solution.solve_part_one())
        typer.echo("- Part One: {result}".format(result=solution_result))
        solution_result = SolutionResult(self._solution.solve_part_two())
        typer.echo("- Part Two: {result}".format(result=solution_result))

    def benchmark(self, iterations: int = 1) -> None:
        typer.echo("Benchmarking {name}".format(name=self._solution.solution_name))
        solution_time = _benchmark(
            name="- Part One:",
            func=self._solution.solve_part_one,
            iterations=iterations,
        )
        typer.secho(solution_time, fg=_get_color(solution_time))
        solution_time = _benchmark(
            name="- Part Two:",
            func=self._solution.solve_part_two,
            iterations=iterations,
        )
        typer.secho(solution_time, fg=_get_color(solution_time))


def _benchmark(
    name: str,
    func: Callable[[], int | str],
    iterations: int = 1,
) -> str:
    with typer.progressbar(
        range(iterations),
        label=name,
        update_min_steps=int(math.ceil(iterations / 100)),
    ) as progress:
        start = time.perf_counter_ns()

        for _ in progress:
            func()

        end = time.perf_counter_ns()

    total = end - start
    average = _get_human_readable_time(total / iterations)

    return "-- Average {time}".format(time=average)


def _get_human_readable_time(nanoseconds: float) -> str:
    unit = "ns"
    humanized = nanoseconds

    if humanized > 1000:
        humanized /= 1000
        unit = "µs"

    if humanized > 1000:
        humanized /= 1000
        unit = "ms"

    if humanized > 1000:
        humanized /= 1000
        unit = "s"

    humanized = round(humanized, 2)

    return "{time} {unit}".format(time=humanized, unit=unit)


def _get_color(average_time: str) -> str:
    if "ns" in average_time:
        return typer.colors.CYAN

    if "µs" in average_time:
        return typer.colors.GREEN

    if "ms" in average_time:
        return typer.colors.YELLOW

    return typer.colors.RED
