import re

from aoc import solution

_MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

_PART_ONE_PATTERN = digit_pattern = re.compile(r"(\d)")
_PART_TWO_FIRST_DIGIT_PATTERN = re.compile(r"(\d|{0})".format("|".join(_MAPPING)))
_PART_TWO_LAST_DIGIT_PATTERN = re.compile(r"(?s:.*)(\d|{0})".format("|".join(_MAPPING)))


class Solution(solution.Solution):
    day: int = 1
    year: int = 2023
    name: str = "Trebuchet?!"

    def solve_part_one(self) -> int:
        return sum(_calibration_value_part_one(line) for line in self._input_lines)

    def solve_part_two(self) -> int:
        return sum(_calibration_value_part_two(line) for line in self._input_lines)


def _calibration_value_part_one(line: str) -> int:
    matches = re.findall(_PART_ONE_PATTERN, line)
    return int("{0}{1}".format(matches[0], matches[-1]))


def _calibration_value_part_two(line: str) -> int:
    first_digit_match = re.search(_PART_TWO_FIRST_DIGIT_PATTERN, line)
    last_digit_match = re.search(_PART_TWO_LAST_DIGIT_PATTERN, line)

    if not first_digit_match or not last_digit_match:
        return 0

    first_digit = _MAPPING.get(first_digit_match.group(1), first_digit_match.group(1))
    last_digit = _MAPPING.get(last_digit_match.group(1), last_digit_match.group(1))

    return int("{0}{1}".format(first_digit, last_digit))
