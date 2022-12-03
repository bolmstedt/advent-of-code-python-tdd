import pytest

from aoc import loader
from aoc.year_2022.day_02_rock_paper_scissors import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("B X", 1),
        ("C Y", 2),
        ("A Z", 3),
    ],
)
def test_move_scores(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("B X", 1),
        ("A X", 4),
        ("C X", 7),
    ],
)
def test_round_scores(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 15),
        (loader.get_input_data(solution), 14163),
    ],
)
def test_wrong_games(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("B X", 1),
        ("A Y", 4),
        ("C Z", 7),
    ],
)
def test_reactive_scores(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        (loader.get_module_data(solution, "fixture.txt"), 12),
        (loader.get_input_data(solution), 12091),
    ],
)
def test_correct_games(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected
