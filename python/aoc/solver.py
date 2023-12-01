import time
from collections.abc import Callable

import typer
from rich import progress

from aoc import solution


class SolutionError(Exception):
    """Raised when a solution is broken."""


class SolutionResult(object):
    def __init__(self, solution_result: int | str):
        self._solution_result = solution_result

    def __hash__(self) -> int:
        return hash(str(self))

    def __str__(self) -> str:
        return str(self._solution_result)

    def __repr__(self) -> str:
        return str(self._solution_result)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, str | int):
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

    def benchmark(self, iterations: int = 1, timeout: float = 0.1) -> None:
        typer.echo("Benchmarking {name}".format(name=self._solution.solution_name))

        try:
            solution_time = _benchmark(
                name="- Part One:",
                func=self._solution.solve_part_one,
                iterations=iterations,
                timeout=timeout,
            )
        except SolutionError as err:
            typer.secho(str(err), fg=typer.colors.RED)
        else:
            typer.secho(solution_time, fg=_get_color(solution_time))

        try:
            solution_time = _benchmark(
                name="- Part Two:",
                func=self._solution.solve_part_two,
                iterations=iterations,
                timeout=timeout,
            )
        except SolutionError as err:
            typer.secho(str(err), fg=typer.colors.RED)
        else:
            typer.secho(solution_time, fg=_get_color(solution_time))


def _benchmark(
    name: str,
    func: Callable[[], int | str],
    iterations: int = 1,
    timeout: float = 0.2,
) -> str:
    max_total_time = iterations * timeout * 1000000000
    total = 0
    iteration = 0
    progress_bar = progress.track(
        sequence=range(iterations),
        description=name,
        total=iterations,
        transient=True,
    )

    for _ in progress_bar:
        iteration += 1
        start = time.perf_counter_ns()
        try:
            func()
        except Exception as err:  # noqa: BLE001
            raise SolutionError("Solution is broken") from err

        end = time.perf_counter_ns()
        total += end - start

        if total > max_total_time:
            break

    average = _get_human_readable_time(total / iteration)

    return "{name} {time}".format(name=name, time=average)


def _get_human_readable_time(nanoseconds: float) -> str:
    unit = "ns"
    humanized = nanoseconds

    if humanized > 1000:
        humanized /= 1000
        unit = "μs"

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

    if "μs" in average_time:
        return typer.colors.GREEN

    if "ms" in average_time:
        return typer.colors.YELLOW

    return typer.colors.RED
