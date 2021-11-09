import datetime
from typing import Optional

import typer

import downloader

app = typer.Typer()


@app.command()
def benchmark() -> None:
    typer.echo("Benchmarking")


@app.command()
def generate(year: Optional[int] = None, day: Optional[int] = None) -> None:
    if not year:
        year = datetime.datetime.now().year

    if not day:
        day = datetime.datetime.now().day

    downloader.download(year=year, day=day)


if __name__ == "__main__":
    app()
