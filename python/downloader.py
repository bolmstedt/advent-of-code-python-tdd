import html
import pathlib
import re

import requests
import typer

AOC_WEB = "https://adventofcode.com/{year}/day/{day}"
_BUILD_FILE = """python_sources()
"""
_BUILD_FILE_WITH_TESTS = """python_sources()

python_tests(name="tests")
"""


def download(year: int, day: int) -> None:
    name_raw = _get_day_name(year=year, day=day)
    padded_day = str(day).rjust(2, "0")

    day_name = "day_{day}_{name}".format(day=padded_day, name=_name_to_slug(name_raw))
    folder = pathlib.Path(
        "python/year_{year}/{day_name}".format(year=year, day_name=day_name),
    )
    _create_solution_path(folder)
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
    _create_file(pathlib.Path(folder.parent, "__init__.py"))
    _create_file(pathlib.Path(folder.parent, "BUILD"), _BUILD_FILE)
    _create_file(pathlib.Path(folder, "__init__.py"))
    _create_file(pathlib.Path(folder, "BUILD"), _BUILD_FILE_WITH_TESTS)
    _create_file(pathlib.Path(folder, "solution.py"))
    _create_file(pathlib.Path(folder, "solution_test.py"))


def _create_file(file_path: pathlib.Path, file_content: str = "") -> None:
    if not file_path.exists():
        with file_path.open(mode="w") as file_handle:
            file_handle.write(file_content)
            typer.echo("Created {file_path}".format(file_path=file_path))
