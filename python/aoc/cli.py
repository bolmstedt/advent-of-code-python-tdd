import datetime
import pathlib
from typing import Optional

import typer

from aoc import downloader, loader

app = typer.Typer()


@app.command()
def solve(benchmark: Optional[bool] = False, iterations: int = 100) -> None:
    folder = pathlib.Path(__file__).parent

    for day in folder.glob("year_*/*/solution.py"):
        solver = loader.create_solver(day)

        if benchmark:
            solver.benchmark(iterations)
        else:
            solver.solve()


@app.command()
def generate(year: Optional[int] = None, day: Optional[int] = None) -> None:
    if not year:
        year = datetime.datetime.now().year

    if not day:
        day = datetime.datetime.now().day

    downloader.download(year=year, day=day)


if __name__ == "__main__":
    app()
