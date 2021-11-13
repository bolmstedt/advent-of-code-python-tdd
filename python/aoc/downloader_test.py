import pathlib
from http import HTTPStatus

import pytest
import requests_mock as req_mock
import typer
from pyfakefs import fake_filesystem

from aoc import downloader

_RESPONSE = "<h2>--- Day 1: Foo @ Bar (Baz)---</h2>"
_TEST_YEAR = 2015
_TEST_DAY = 1
_TEST_URL = downloader.AOC_WEB.format(year=_TEST_YEAR, day=_TEST_DAY)
_TEST_YEAR_FOLDER = "python/aoc/year_2015"
_TEST_DAY_FOLDER = "{folder}/day_01_foo_bar_baz".format(folder=_TEST_YEAR_FOLDER)


def test_invalid_day_throws_error(requests_mock: req_mock.Mocker) -> None:
    requests_mock.get(_TEST_URL, status_code=HTTPStatus.NOT_FOUND)

    with pytest.raises(typer.Abort):
        downloader.download(year=_TEST_YEAR, day=_TEST_DAY)


def test_year_folder_is_created(
    requests_mock: req_mock.Mocker,
    fs: fake_filesystem.FakeFilesystem,
) -> None:
    year_folder = pathlib.Path(_TEST_YEAR_FOLDER)
    assert not year_folder.is_dir()
    requests_mock.get(_TEST_URL, text=_RESPONSE)
    downloader.download(year=_TEST_YEAR, day=_TEST_DAY)
    assert year_folder.is_dir()


def test_day_folder_is_created(
    requests_mock: req_mock.Mocker,
    fs: fake_filesystem.FakeFilesystem,
) -> None:
    day_folder = pathlib.Path(_TEST_DAY_FOLDER)
    assert not day_folder.is_dir()
    requests_mock.get(_TEST_URL, text=_RESPONSE)
    downloader.download(year=_TEST_YEAR, day=_TEST_DAY)
    assert day_folder.is_dir()


@pytest.mark.parametrize(
    "file_path",
    (
        "{folder}/__init__.py".format(folder=_TEST_YEAR_FOLDER),
        "{folder}/BUILD".format(folder=_TEST_YEAR_FOLDER),
        "{folder}/__init__.py".format(folder=_TEST_DAY_FOLDER),
        "{folder}/BUILD".format(folder=_TEST_DAY_FOLDER),
        "{folder}/solution.py".format(folder=_TEST_DAY_FOLDER),
        "{folder}/solution_test.py".format(folder=_TEST_DAY_FOLDER),
        "{folder}/input.txt".format(folder=_TEST_DAY_FOLDER),
    ),
)
def test_file_is_created(
    requests_mock: req_mock.Mocker,
    fs: fake_filesystem.FakeFilesystem,
    file_path: str,
) -> None:
    file_path_to_test = pathlib.Path(file_path)
    assert not file_path_to_test.exists()
    requests_mock.get(_TEST_URL, text=_RESPONSE)
    downloader.download(year=_TEST_YEAR, day=_TEST_DAY)
    assert file_path_to_test.exists()
