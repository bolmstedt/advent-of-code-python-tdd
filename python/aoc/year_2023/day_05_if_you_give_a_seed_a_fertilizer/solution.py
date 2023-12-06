import copy
from typing import NamedTuple

import more_itertools

from aoc import solution


class Mapping(NamedTuple):
    source: range
    shift: int


class Map(NamedTuple):
    name: str
    mappings: list[Mapping]


class Solution(solution.Solution):
    day: int = 5
    year: int = 2023
    name: str = "If You Give A Seed A Fertilizer"

    def solve_part_one(self) -> int:
        return min(self._apply_soil_mappings(self._get_soils()))

    def solve_part_two(self) -> int:
        mapped = self._apply_range_mappings(self._get_soil_ranges())

        if not mapped:
            return -1

        return min(soil.start for soil in mapped if soil.start > 0)

    def _get_soils(self) -> set[int]:
        return set(map(int, self._input_lines[0][7:].split(" ")))

    def _get_soil_ranges(self) -> list[range]:
        soils = [
            range(soil, soil + length)
            for soil, length in more_itertools.chunked(
                map(int, self._input_lines[0][7:].split(" ")),
                2,
            )
        ]
        soils.sort(key=lambda x: x.start)

        return soils

    def _apply_soil_mappings(self, soils: set[int]) -> set[int]:
        current_soils = copy.copy(soils)
        mapped_soils: set[int] = set()
        unmapped_soils = copy.copy(current_soils)

        for line in self._input_lines[1:]:
            if not line or ":" in line:
                if mapped_soils:
                    current_soils = mapped_soils.union(unmapped_soils)
                    unmapped_soils = copy.copy(current_soils)
                    mapped_soils = set()

                continue

            destination, source, length = map(int, line.split(" "))
            source_range = range(source, source + length)

            for soil in current_soils:
                if soil in source_range:
                    unmapped_soils.remove(soil)
                    mapped_soils.add(destination + abs(source - soil))

        if mapped_soils:
            current_soils = mapped_soils.union(unmapped_soils)

        return current_soils

    def _apply_range_mappings(self, soils: list[range]) -> list[range]:
        for soil_map in self._create_maps():
            soils = apply_range_map(soils, soil_map)

        return soils

    def _create_maps(self) -> list[Map]:
        maps = []
        map_name = ""
        mappings: list[Mapping] = []

        for line in self._input_lines[1:]:
            if ":" in line:
                map_name = line[:-1]
                continue

            if not line:
                if mappings:
                    mappings.sort(key=lambda x: x.source.start)
                    maps.append(
                        Map(
                            name=map_name,
                            mappings=mappings,
                        ),
                    )
                    mappings = []

                continue

            destination, source, length = map(int, line.split(" "))
            mappings.append(
                Mapping(
                    source=range(source, source + length),
                    shift=destination - source,
                ),
            )

        if mappings:
            mappings.sort(key=lambda x: x.source.start)
            maps.append(
                Map(
                    name=map_name,
                    mappings=mappings,
                ),
            )

        return maps


def apply_range_map(soils: list[range], soil_map: Map) -> list[range]:
    soils_to_shift = []

    for mapping in soil_map.mappings:
        for index, soil in enumerate(soils):
            overlap = range_overlap(soil, mapping.source)

            if overlap:
                soils.pop(index)
                if overlap.start > soil.start:
                    soils.append(range(soil.start, overlap.start))

                soils_to_shift.append(overlap)

                if overlap.stop < soil.stop:
                    soils.append(range(overlap.stop, soil.stop))

    soils.extend(
        _shift_range(soil, mapping.shift)
        for mapping in soil_map.mappings
        for soil in soils_to_shift
        if range_overlap(soil, mapping.source)
    )

    return soils


def _shift_range(range_: range, shift: int) -> range:
    return range(range_.start + shift, range_.stop + shift)


def range_overlap(first: range, second: range) -> range:
    return range(max(first.start, second.start), min(first.stop, second.stop))
