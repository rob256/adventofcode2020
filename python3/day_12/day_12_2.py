from enum import Enum
from typing import List, Tuple


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
    waypoint_ns = 1
    waypoint_ew = 10
    ship_ns = 0
    ship_ew = 0

    for instruction in instructions:
        command, value = instruction[0], int(instruction[1:])
        if command == "N":
            waypoint_ns += value
        if command == "E":
            waypoint_ew += value
        if command == "S":
            waypoint_ns -= value
        if command == "W":
            waypoint_ew -= value
        if command == "F":
            ship_ns += value * waypoint_ns
            ship_ew += value * waypoint_ew
        if command == "R":
            for _ in range(value // 90):
                waypoint_ew, waypoint_ns = waypoint_ns, waypoint_ew * -1
        if command == "L":
            for _ in range(value // 90):
                waypoint_ew, waypoint_ns = waypoint_ns * -1, waypoint_ew
    return ship_ns, ship_ew
            


if __name__ == "__main__":
    solve()