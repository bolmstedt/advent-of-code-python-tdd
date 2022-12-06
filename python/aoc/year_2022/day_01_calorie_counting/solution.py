from aoc import solution


class Solution(solution.Solution):
    day: int = 1
    year: int = 2022
    name: str = "Calorie Counting"

    def solve_part_one(self) -> int:
        return max(self._get_calories_per_elf())

    def solve_part_two(self) -> int:
        return sum(sorted(self._get_calories_per_elf(), reverse=True)[:3])

    def _get_calories_per_elf(self) -> list[int]:
        calories_by_elf = []
        calories = 0

        for carried in self._input_lines:
            if carried == "":
                calories_by_elf.append(calories)
                calories = 0
                continue

            calories += int(carried)

        if calories:
            calories_by_elf.append(calories)

        return calories_by_elf
