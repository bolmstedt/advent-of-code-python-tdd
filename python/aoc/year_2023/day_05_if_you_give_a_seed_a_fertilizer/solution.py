import copy

from aoc import solution


class Solution(solution.Solution):
    day: int = 5
    year: int = 2023
    name: str = "If You Give A Seed A Fertilizer"

    def solve_part_one(self) -> int:
        return min(self._apply_soil_mappings(self._get_soils()))

    def solve_part_two(self) -> int:
        return -1

    def _get_soils(self) -> set[int]:
        return set(map(int, self._input_lines[0][7:].split(" ")))

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
