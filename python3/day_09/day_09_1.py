from typing import List


def solve():
    numbers_list = get_numbers_list("input.txt")
    number = get_first_invalid_number(numbers_list, 25)
    print(number)


def get_numbers_list(input_file: str) -> List[int]:
    numbers_list = []
    with open(input_file) as f:
        for line in f:
            numbers_list.append(int(line))
    return numbers_list


def push_to_list(moving_list: List[int], number: int, max_size: int = 25):
    moving_list.append(number)
    if len(moving_list) > max_size:
        moving_list.pop(0)


def has_sum(number_list, total):
    for number in number_list:
        target = total - number
        if target in number_list and number != total / 2:
            return True
    return False


def get_first_invalid_number(numbers_list: List[int], preamble: int) -> int:
    moving_list = []
    for i, number in enumerate(numbers_list):
        if i >= preamble:
            if not has_sum(moving_list, number):
                return number
        push_to_list(moving_list, number, preamble)
    raise ValueError("No invalid number found.")
            

if __name__ == "__main__":
    solve()