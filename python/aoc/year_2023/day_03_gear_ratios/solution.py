import re
from typing import NamedTuple

from aoc import solution

_PARTS_PATTERN = re.compile(r"(\d+)")
_SYMBOL_PATTERN = re.compile(r"[^\d.]")
_GEARS_PATTERN = re.compile(r"(\*)")


class Part(NamedTuple):
    number: int
    line: int
    span: range


class Gear(NamedTuple):
    line: int
    span: range


class Solution(solution.Solution):
    day: int = 3
    year: int = 2023
    name: str = "Gear Ratios"
    _max_line = 0
    _line_length = 0

    def solve_part_one(self) -> int:
        return sum(
            part.number
            for part in self._parse_parts()
            if self._has_adjacent_symbol(part)
        )

    def _has_adjacent_symbol(self, part: Part) -> bool:
        span = (
            max(part.span.start - 1, 0),
            min(part.span.stop + 2, self._line_length) - 1,
        )
        lines = [self._input_lines[part.line][span[0] : span[1]]]

        if part.line > 0:
            lines.append(self._input_lines[part.line - 1][span[0] : span[1]])

        if part.line != self._max_line:
            lines.append(self._input_lines[part.line + 1][span[0] : span[1]])

        return any(_SYMBOL_PATTERN.search(line) is not None for line in lines)

    def solve_part_two(self) -> int:
        return sum(self._multiple_adjacent_parts(gear) for gear in self._parse_gears())

    def _multiple_adjacent_parts(self, gear: Gear) -> int:
        lines = [self._input_lines[gear.line]]

        if gear.line > 0:
            lines.append(self._input_lines[gear.line - 1])

        if gear.line != self._max_line:
            lines.append(self._input_lines[gear.line + 1])

        possible_parts = [
            part
            for line in lines
            for part in _parse_parts_line(gear.line, line)
            if gear.span.stop >= part.span.start and part.span.stop >= gear.span.start
        ]

        if len(possible_parts) != 2:
            return 0

        return possible_parts[0].number * possible_parts[1].number

    def _parse_parts(self) -> list[Part]:
        self._max_line = len(self._input_lines) - 1
        self._line_length = len(self._input_lines[0])

        return [
            part
            for line_number, line in enumerate(self._input_lines)
            for part in _parse_parts_line(line_number, line)
        ]

    def _parse_gears(self) -> list[Gear]:
        self._max_line = len(self._input_lines) - 1
        self._line_length = len(self._input_lines[0])

        return [
            gear
            for line_number, line in enumerate(self._input_lines)
            for gear in _parse_gears_line(line_number, line)
        ]


def _parse_parts_line(line_number: int, line: str) -> list[Part]:
    return [
        Part(
            number=int(part.group(1)),
            line=line_number,
            span=range(*part.span(1)),
        )
        for part in _PARTS_PATTERN.finditer(line)
    ]


def _parse_gears_line(line_number: int, line: str) -> list[Gear]:
    return [
        Gear(
            line=line_number,
            span=range(*gear.span(0)),
        )
        for gear in _GEARS_PATTERN.finditer(line)
    ]
