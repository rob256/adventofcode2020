from typing import Tuple, List


def solve():
    depart_time, buses = parse_input('input.txt')
    bus = get_bus_with_min_wait(depart_time, buses)
    wait_time = bus - depart_time % bus
    result = wait_time * bus
    print(result)


def parse_input(input_file: str) -> Tuple[int, List[int]]:
    with open(input_file) as f:
        lines = f.readlines()
        depart_time = int(lines[0])
        buses = [int(x) for x in lines[1].split(',') if x != 'x']
        return depart_time, buses


def get_bus_with_min_wait(depart_time: int, buses: List[int]) -> int:
    min_wait = float('inf')
    best_bus = None
    for bus in buses:
        wait_time = bus - depart_time % bus
        if wait_time < min_wait:
            best_bus = bus
            min_wait = wait_time
    return best_bus


if __name__ == "__main__":
    solve()