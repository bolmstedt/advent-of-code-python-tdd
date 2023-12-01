import math

from aoc import solution


class Solution(solution.Solution):
    day: int = 8
    year: int = 2022
    name: str = "Treetop Tree House"

    def solve_part_one(self) -> int:
        side_length = len(self._input_lines)
        border = side_length * 4 - 4

        middle_trees = 0

        for y_pos, row in enumerate(self._input_lines[1:-1], start=1):
            for x_pos, tree in enumerate(row[1:-1], start=1):
                lines_of_sight = [
                    row[:x_pos],
                    row[x_pos + 1 :],
                    [_row[x_pos] for _row in self._input_lines[:y_pos]],
                    [_row[x_pos] for _row in self._input_lines[y_pos + 1 :]],
                ]

                if any(
                    all(tree > comparison for comparison in line)
                    for line in lines_of_sight
                ):
                    middle_trees += 1

        return border + middle_trees

    def solve_part_two(self) -> int:
        viewing_scores = [0]

        for y_pos, row in enumerate(self._input_lines[1:-1], start=1):
            for x_pos, tree in enumerate(row[1:-1], start=1):
                viewing_score = []

                lines_of_sight = [
                    row[:x_pos][::-1],
                    row[x_pos + 1 :],
                    [_row[x_pos] for _row in self._input_lines[:y_pos]][::-1],
                    [_row[x_pos] for _row in self._input_lines[y_pos + 1 :]],
                ]

                for line in lines_of_sight:
                    current = 0

                    for current, comparison in enumerate(line, start=1):
                        if tree > comparison:
                            continue

                        viewing_score.append(current)
                        break
                    else:
                        viewing_score.append(current)

                viewing_scores.append(math.prod(viewing_score))

        return max(viewing_scores)
