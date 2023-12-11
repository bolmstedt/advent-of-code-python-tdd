import pytest

from aoc import loader
from aoc.year_2023.day_11_cosmic_expansion import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("#.\n.#", 2),
        ("#.\n..\n.#", 4),
        ("#..\n..#", 4),
        pytest.param(
            loader.get_module_data(solution, "fixture.txt"),
            374,
            id="fixture",
        ),
        pytest.param(loader.get_input_data(solution), 9965032, id="solution"),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "factor", "expected"),
    [
        pytest.param(
            loader.get_module_data(solution, "fixture.txt"),
            10,
            1030,
            id="fixture*100",
        ),
        pytest.param(
            loader.get_module_data(solution, "fixture.txt"),
            100,
            8410,
            id="fixture*1000",
        ),
        pytest.param(
            loader.get_input_data(solution),
            1000000,
            550358864332,
            id="solution",
        ),
    ],
)
def test_part_two(input_data: str, factor: int, expected: int) -> None:
    assert solution.Solution(input_data).distance_between_galaxies(factor) == expected
