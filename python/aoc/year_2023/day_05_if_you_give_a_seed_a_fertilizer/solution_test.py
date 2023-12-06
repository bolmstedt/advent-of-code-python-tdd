import pytest

from aoc import loader
from aoc.year_2023.day_05_if_you_give_a_seed_a_fertilizer import solution


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("seeds: 1", 1),
        ("seeds: 1 2", 1),
        ("seeds: 1 2\nmap:\n3 1 1", 2),
        ("seeds: 1\nmap:\n3 1 1\n\nmap:\n7 3 1", 7),
        (loader.get_module_data(solution, "fixture.txt"), 35),
        (loader.get_input_data(solution), 462648396),
    ],
)
def test_part_one(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_one() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    [
        ("seeds: 1 2", 1),
        ("seeds: 1 3\nmap:\n3 1 1", 2),
        (loader.get_module_data(solution, "fixture.txt"), 46),
        (loader.get_input_data(solution), 2520479),
    ],
)
def test_part_two(input_data: str, expected: int) -> None:
    assert solution.Solution(input_data).solve_part_two() == expected


@pytest.mark.parametrize(
    ("soils", "soil_map", "expected"),
    [
        (
            [range(1, 10)],
            solution.Map(
                name="foo",
                mappings=[
                    solution.Mapping(source=range(5, 6), shift=10),
                    solution.Mapping(source=range(8, 9), shift=10),
                ],
            ),
            [range(1, 5), range(6, 8), range(9, 10), range(15, 16), range(18, 19)],
        ),
    ],
)
def test_range_application(
    soils: list[range],
    soil_map: solution.Map,
    expected: list[range],
) -> None:
    assert solution.apply_range_map(soils, soil_map) == expected
