import collections

from aoc import solution


class Solution(solution.Solution):
    day: int = 7
    year: int = 2022
    name: str = "No Space Left On Device"
    _part_one_limit = 100000
    _total_space = 70000000
    _needed_space = 30000000

    def solve_part_one(self) -> int:
        return sum(
            filter(
                lambda file_size: file_size < self._part_one_limit,
                self._calculate_directories().values(),
            ),
        )

    def solve_part_two(self) -> int:
        directories = self._calculate_directories()
        free_space = self._total_space - directories["/"]

        if free_space >= self._needed_space:
            return 0

        minimum_to_delete = self._needed_space - free_space

        return min(
            filter(
                lambda file_size: file_size >= minimum_to_delete,
                directories.values(),
            ),
        )

    def _calculate_directories(self) -> dict[str, int]:
        directories: dict[str, int] = collections.defaultdict(int)
        current: list[str] = []

        for line in self._input_lines:
            if line[0] not in {"$", "d"}:
                filesize = int(line.split(" ")[0])

                for folder in current:
                    directories[folder] += filesize

                continue

            if line[2] != "c":
                continue

            match line[5]:
                case "/":
                    current = ["/"]
                case ".":
                    current.pop()
                case _:
                    current.append(current[-1] + line[5:])

        return directories
