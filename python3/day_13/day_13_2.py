from typing import Tuple, List
from math import gcd


def solve():
    buses = parse_input('input.txt')
    # buses = list(map(int, '67,7,59,61'.split(',')))
    current = 0
    current_diff = buses[0]
    for _i, bus in enumerate(buses[1:]):
        i = _i + 1
        while (current + i) % bus != 0:
            current += current_diff
        print(f's3: {current}')
        current_diff *= bus
    print(current)


def parse_input(input_file: str) -> Tuple[int, List[int]]:
    buses = []
    with open(input_file) as f:
        lines = f.readlines()
        for bus in lines[1].split(','):
            if bus == 'x':
                buses.append(1)
            else:
                buses.append(int(bus))
    return buses


if __name__ == "__main__":
    solve()
