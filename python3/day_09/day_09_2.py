from typing import List


def solve():
    numbers_list = get_numbers_list("input.txt")
    number = get_first_invalid_number(numbers_list, 25)
    encryption_weakness = get_encryption_weakness(numbers_list, number)
    print(encryption_weakness)


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


def get_encryption_weakness(numbers_list: List[int], target_number: int) -> int:
    i1 = 0
    i2 = 1
    total = numbers_list[i1] + numbers_list[i2]
    while True:
        print(f"{i1} {i2} = {total}")
        if i1 == i2 or total < target_number:
            i2 += 1
            total += numbers_list[i2]
        elif total > target_number:
            total -= numbers_list[i1]
            i1 += 1
        else:
            print(f"Found sum with numbers from {numbers_list[i1]} to {numbers_list[i2]}")
            return min(numbers_list[i1:i2 + 1]) + max(numbers_list[i1:i2 +1])
        


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