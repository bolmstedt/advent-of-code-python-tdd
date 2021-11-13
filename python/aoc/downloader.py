import html
import pathlib
import re

import requests
import typer

from aoc import loader, templates

AOC_WEB = "https://adventofcode.com/{year}/day/{day}"


def download(year: int, day: int) -> None:
    name_raw = _get_day_name(year=year, day=day)
    padded_day = str(day).rjust(2, "0")

    day_name = "day_{day}_{name}".format(day=padded_day, name=_name_to_slug(name_raw))
    folder = pathlib.Path(
        "python/aoc/year_{year}/{day_name}".format(year=year, day_name=day_name),
    )
    _create_solution_path(folder)
    _create_file(pathlib.Path(folder.parent, "__init__.py"))
    _create_file(
        pathlib.Path(folder.parent, "BUILD"),
        loader.get_module_data(templates, "BUILD_YEAR"),
    )
    _create_file(pathlib.Path(folder, "__init__.py"))
    _create_file(
        pathlib.Path(folder, "BUILD"),
        loader.get_module_data(templates, "BUILD_DAY"),
    )
    solution = loader.get_module_data(templates, "solution.py")
    solution = solution.replace("1111", str(day))
    solution = solution.replace("2222", str(year))
    solution = solution.replace("__NAME__", str(name_raw))
    _create_file(pathlib.Path(folder, "solution.py"), solution)
    _create_file(pathlib.Path(folder, "solution_test.py"))
    _create_file(pathlib.Path(folder, "input.txt"))
    typer.echo(
        "Generated {year}:{day} - {name}".format(
            year=year,
            day=padded_day,
            name=name_raw,
        ),
    )


def _get_day_name(year: int, day: int) -> str:
    url = AOC_WEB.format(year=year, day=day)
    response = requests.get(url)
    match = re.search(r"<h2>--- Day \d{1,2}:(.*)---</h2>", response.text)

    if not match:
        typer.secho(
            "Error downloading {url}".format(url=url),
            fg=typer.colors.RED,
        )
        raise typer.Abort()

    return html.unescape(match.group(1).strip())


def _name_to_slug(raw_name: str) -> str:
    return re.sub(
        r"[^\w]",
        "",
        raw_name.lower().replace(" ", "_").replace("-", "_"),
    ).replace("__", "_")


def _create_solution_path(folder: pathlib.Path) -> None:
    folder.mkdir(parents=True, exist_ok=True)
    typer.echo("Created {folder}".format(folder=folder))


def _create_file(file_path: pathlib.Path, file_content: str = "") -> None:
    if not file_path.exists():
        with file_path.open(mode="w") as file_handle:
            file_handle.write(file_content)
            typer.echo("Created {file_path}".format(file_path=file_path))
