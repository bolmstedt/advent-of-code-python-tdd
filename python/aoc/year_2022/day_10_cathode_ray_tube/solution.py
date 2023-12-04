from aoc import solution


class Solution(solution.Solution):
    day: int = 10
    year: int = 2022
    name: str = "Cathode-Ray Tube"

    def solve_part_one(self) -> int:
        memory = self._fill_memory()

        return sum(cycle * memory[cycle - 1] for cycle in [20, 60, 100, 140, 180, 220])

    def solve_part_two(self) -> str:
        memory = self._fill_memory()
        screen = ""

        for cycle, register in enumerate(memory, start=0):
            pixel = cycle % 40

            if pixel == 0:
                screen += "\n"

            draw = "#" if -1 <= pixel - register <= 1 else "."

            screen += draw

        return screen

    def _fill_memory(self) -> list[int]:
        memory = []
        x = 1
        cycle = 0

        for operation in self._input_lines:
            memory.append(x)
            cycle += 1

            if operation == "noop":
                continue

            memory.append(x)
            cycle += 1
            x += int(operation[5:])

        return memory
