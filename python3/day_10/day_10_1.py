from typing import List, Tuple


def solve():
    adapters = get_adapters("input.txt")
    diff_1, diff_3 = get_voltage_differences(adapters)
    return diff_1 * diff_3


def get_adapters(input_file: str) -> List[int]:
    numbers = []
    with open(input_file) as f:
        for line in f:
            numbers.append(int(line))
    return sorted(numbers)


def get_voltage_differences(adapters: List[int]) -> Tuple[int, int]:
    diff_1 = 0
    diff_3 = 1
    current = 0
    for adapter in adapters:
        if adapter - current == 3:
            diff_3 += 1
        elif adapter - current == 1:
            diff_1 += 1
        elif adapter - current > 3:
            raise ValueError('adapter not in range')
        current = adapter
    return diff_1, diff_3


if __name__ == "__main__":
    print(solve())