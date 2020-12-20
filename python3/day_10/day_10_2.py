from typing import List, Tuple


def solve():
    adapters = get_adapters("input.txt")
    number_of_arrangements = count_possible_arrangements([0] + adapters)
    return number_of_arrangements


def get_adapters(input_file: str) -> List[int]:
    numbers = []
    with open(input_file) as f:
        for line in f:
            numbers.append(int(line))
    return sorted(numbers)


def count_possible_arrangements(adapters: List[int], current_number: int = 0, cache={}) -> int:
    if len(adapters) == 0:
        return 1

    if adapters[0] - current_number > 3:
        return 0
    
    if (current_number, adapters[0]) in cache:
        return cache[(current_number, adapters[0])]
    
    total = 0
    total += count_possible_arrangements(adapters[1:], adapters[0])

    if len(adapters) > 2:
        total += count_possible_arrangements(adapters[2:], adapters[0])
    
    if len(adapters) > 3:
        total += count_possible_arrangements(adapters[3:], adapters[0])
    
    cache[(current_number, adapters[0])] = total

    return total


if __name__ == "__main__":
    print(solve())
