from typing import TypeAlias

from aoc import solution

_Coordinates: TypeAlias = tuple[int, int]

_PIPES_MAP = {
    "|": {"N": "N", "S": "S"},
    "-": {"E": "E", "W": "W"},
    "L": {"N": "W", "E": "S"},
    "J": {"N": "E", "W": "S"},
    "7": {"S": "E", "W": "N"},
    "F": {"S": "W", "E": "N"},
}


class Solution(solution.Solution):
    day: int = 10
    year: int = 2023
    name: str = "Pipe Maze"

    def solve_part_one(self) -> int:
        return len(self._find_loop()) // 2

    def solve_part_two(self) -> int:
        loop = self._find_loop()
        loop_length = len(loop)
        loop.append(loop[0])
        loop_area = abs(
            sum(
                loop[index][0] * loop[index + 1][1]
                - loop[index][1] * loop[index + 1][0]
                for index in range(loop_length)
            ),
        )

        return (loop_area - loop_length) // 2 + 1

    def _find_loop(self) -> list[_Coordinates]:
        start = self._find_start()

        for entrypoint, pipe in self._find_connected_pipes(start).items():
            loop = self._find_loop_length(pipe, entrypoint, start)

            if loop:
                return loop

        raise RuntimeError("No loop found")

    def _find_start(self) -> _Coordinates:
        for y_pos, line in enumerate(self._input_lines):
            try:
                x_pos = line.index("S")
            except ValueError:
                continue
            else:
                return x_pos, y_pos

        raise RuntimeError("No start found")

    def _find_connected_pipes(self, pipe: _Coordinates) -> dict[str, _Coordinates]:
        pipes = {}

        if pipe[0] != 0 and self._input_lines[pipe[1]][pipe[0] - 1] in {"-", "L", "F"}:
            pipes["E"] = (pipe[0] - 1, pipe[1])

        if pipe[0] < len(self._input_lines[0]) and self._input_lines[pipe[1]][
            pipe[0] + 1
        ] in {"-", "J", "7"}:
            pipes["W"] = (pipe[0] + 1, pipe[1])

        if pipe[1] != 0 and self._input_lines[pipe[1] - 1][pipe[0]] in {"|", "7", "F"}:
            pipes["S"] = (pipe[0], pipe[1] - 1)

        if pipe[1] < len(self._input_lines) and self._input_lines[pipe[1] + 1][
            pipe[0]
        ] in {"|", "L", "J"}:
            pipes["N"] = (pipe[0], pipe[1] + 1)

        return pipes

    def _find_loop_length(
        self,
        start: _Coordinates,
        entrypoint: str,
        end: _Coordinates,
    ) -> list[_Coordinates] | None:
        loop = [start]
        position = start

        while position != end:
            try:
                current_pipe = self._input_lines[position[1]][position[0]]
            except IndexError:
                return None

            try:
                entrypoint = _PIPES_MAP[current_pipe][entrypoint]
            except KeyError:
                return None

            match entrypoint:
                case "N":
                    position = (position[0], position[1] + 1)
                case "S":
                    position = (position[0], position[1] - 1)
                case "W":
                    position = (position[0] + 1, position[1])
                case "E":
                    position = (position[0] - 1, position[1])

            loop.append(position)

        return loop
