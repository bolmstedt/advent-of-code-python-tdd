import math

from aoc import solution


class Nodes(object):
    def __init__(
        self,
        nodes: dict[str, tuple[str, str]],
        instructions: tuple[int, ...],
    ):
        self._raw_nodes = nodes
        self._instructions = instructions
        self.length = len(instructions)
        self._node_map = {node: index for index, node in enumerate(nodes.keys())}
        self._nodes = tuple(
            (self._node_map[node[0]], self._node_map[node[1]])
            for node in nodes.values()
        )

    def steps_to_goal(
        self,
        start: str,
        ends: set[str],
    ) -> int:
        steps = 0
        position = self._node_map[start]
        destinations = {self._node_map[end] for end in ends}

        while position not in destinations:
            position = self._nodes[position][self._instructions[steps % self.length]]
            steps += 1

        return steps


class Solution(solution.Solution):
    day: int = 8
    year: int = 2023
    name: str = "Haunted Wasteland"

    def solve_part_one(self) -> int:
        nodes = Nodes(self._parse_nodes(), self._parse_instructions())

        return nodes.steps_to_goal(start="AAA", ends={"ZZZ"})

    def solve_part_two(self) -> int:
        raw_nodes = self._parse_nodes()
        nodes = Nodes(raw_nodes, self._parse_instructions())
        starts = {node for node in raw_nodes if node.endswith("A")}
        ends = {node for node in raw_nodes if node.endswith("Z")}

        return math.lcm(*(nodes.steps_to_goal(start, ends) for start in starts))

    def _parse_instructions(self) -> tuple[int, ...]:
        return tuple(0 if direction == "L" else 1 for direction in self._input_lines[0])

    def _parse_nodes(self) -> dict[str, tuple[str, str]]:
        return {line[0:3]: (line[7:10], line[12:15]) for line in self._input_lines[2:]}
