import datetime
import pathlib

import typer

from aoc import downloader, loader

app = typer.Typer()


@app.command()
def solve(
    year: str = "*",
    day: str = "*",
    iterations: int = 100,
    *,
    today: bool | None = False,
    benchmark: bool | None = False,
) -> None:
    if today:
        now = datetime.datetime.now(tz=datetime.UTC)
        year = str(now.year)
        day = str(now.day)

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
def generate(year: int | None = None, day: int | None = None) -> None:
    now = datetime.datetime.now(tz=datetime.UTC)
    year = year or now.year
    day = day or now.day
    downloader.download(year=year, day=day)


if __name__ == "__main__":
    app()
