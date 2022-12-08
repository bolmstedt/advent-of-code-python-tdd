import datetime
import pathlib
from typing import Optional

import typer

from aoc import downloader, loader

app = typer.Typer()


@app.command()
def solve(
    today: Optional[bool] = False,
    year: str = "*",
    day: str = "*",
    benchmark: Optional[bool] = False,
    iterations: int = 100,
) -> None:
    if today:
        year = str(datetime.datetime.now().year)
        day = str(datetime.datetime.now().day)

    if day != "*":
        day = day.zfill(2)

    if year != "*" and len(year) == 2:
        year = "20{year}".format(year=year)

    path = "year_{year}/day_{day}_*/solution.py".format(year=year, day=day)

    for day_solution in sorted(pathlib.Path(__file__).parent.glob(path)):
        solver = loader.create_solver(day_solution)

        if benchmark:
            solver.benchmark(iterations)
        else:
            solver.solve()


@app.command()
def generate(year: Optional[int] = None, day: Optional[int] = None) -> None:
    year = year or datetime.datetime.now().year
    day = day or datetime.datetime.now().day
    downloader.download(year=year, day=day)


if __name__ == "__main__":
    app()
