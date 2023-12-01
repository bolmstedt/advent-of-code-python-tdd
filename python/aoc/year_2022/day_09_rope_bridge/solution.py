import itertools

from aoc import solution


class Solution(solution.Solution):
    day: int = 9
    year: int = 2022
    name: str = "Rope Bridge"

    def solve_part_one(self) -> int:
        return self._calculate_tail_visits(2)

    def solve_part_two(self) -> int:
        return self._calculate_tail_visits(10)

    def _calculate_tail_visits(self, number_of_knots: int) -> int:
        memory = {(0, 0)}
        knots = [[0, 0] for _ in range(number_of_knots)]

        for line in self._input_lines:
            direction, steps = line.split(" ")

            for _ in range(int(steps)):
                match direction:
                    case "L":
                        knots[0][0] -= 1
                    case "R":
                        knots[0][0] += 1
                    case "U":
                        knots[0][1] -= 1
                    case "D":
                        knots[0][1] += 1

                for head, tail in itertools.pairwise(knots):
                    if abs(head[1] - tail[1]) < 2 and abs(head[0] - tail[0]) < 2:
                        continue

                    if head[1] == tail[1]:
                        tail[0] += max(-1, min(1, head[0] - tail[0]))
                    elif head[0] == tail[0]:
                        tail[1] += max(-1, min(1, head[1] - tail[1]))
                    else:
                        tail[0] += max(-1, min(1, head[0] - tail[0]))
                        tail[1] += max(-1, min(1, head[1] - tail[1]))

                memory.add((knots[-1][0], knots[-1][1]))

        return len(memory)
