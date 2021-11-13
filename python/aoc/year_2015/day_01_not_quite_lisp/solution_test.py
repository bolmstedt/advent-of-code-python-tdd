import pytest

from aoc import loader
from aoc.year_2015.day_01_not_quite_lisp import solution


@pytest.mark.parametrize(
    ("test_data", "expected"),
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
        (loader.get_input_data(solution), 138),
    ],
)
def test_floor_is_reached(test_data: str, expected: int) -> None:
    assert solution.Solution(test_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("test_data", "expected"),
    [
        (")", 1),
        ("()())", 5),
        ("())()()", 3),
        (loader.get_input_data(solution), 1771),
    ],
)
def test_cellar_is_reached_at_position(test_data: str, expected: int) -> None:
    assert solution.Solution(test_data).solve_part_two() == expected


def test_cellar_is_never_reached() -> None:
    with pytest.raises(solution.NeverReachedCellarError):
        solution.Solution("(").solve_part_two()
