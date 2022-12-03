from aoc import solution_helpers


class Solution(solution_helpers.Solution):
    day: int = 2
    year: int = 2021
    name: str = "Dive!"

    def _solve_part_one(self) -> int:
        depth = 0
        horizontal = 0

        for command in self._input_lines:
            operation, distance = command.split(" ")

            match operation:
                case "forward":
                    horizontal += int(distance)
                case "up":
                    depth -= int(distance)
                case "down":
                    depth += int(distance)

        return depth * horizontal

    def _solve_part_two(self) -> int:
        dive = _Dive()

        for command in self._input_lines:
            operation, distance = command.split(" ")
            dive.move(operation, int(distance))

        return dive.depth * dive.horizontal


class _Dive(object):
    def __init__(self) -> None:
        self._aim = 0
        self.depth = 0
        self.horizontal = 0

    def move(self, operation: str, distance: int) -> None:
        match operation:
            case "forward":
                self.horizontal += distance
                self.depth += self._aim * distance
            case "up":
                self._aim -= distance
            case "down":
                self._aim += distance
