from enum import Enum
from typing import List, Tuple


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


DIRECTION_MULTIPLIERS = {
    Direction.NORTH: (1, 0),
    Direction.EAST: (0, 1),
    Direction.SOUTH: (-1, 0),
    Direction.WEST: (0, -1),
}


def solve():
    instructions = get_instructions('input.txt')
    ew_position, ns_position = get_position(instructions)
    print(abs(ew_position) + abs(ns_position))


def get_instructions(input_file: str) -> List[str]:
    instructions = []
    with open(input_file) as f:
        for line in f:
            instructions.append(line.strip())
    return instructions


def get_position(instructions: List[str]) -> Tuple[int ,int]:
    ns = 0
    ew = 0
    facing = Direction.EAST

    for instruction in instructions:
        command, value = instruction[0], int(instruction[1:])
        if command == "N":
            ns += value
        if command == "E":
            ew += value
        if command == "S":
            ns -= value
        if command == "W":
            ew -= value
        if command == "F":
            _ns, _ew = DIRECTION_MULTIPLIERS[facing]
            ns += value * _ns
            ew += value * _ew
        if command == "R":
            rotate = value // 90
            facing = facing.value + rotate
            facing = facing % 4
            facing = Direction(facing)
        if command == "L":
            rotate = value // 90
            facing = facing.value - rotate
            facing = facing % 4
            facing = Direction(facing)
    return ns, ew
            


if __name__ == "__main__":
    solve()