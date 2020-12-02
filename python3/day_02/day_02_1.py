from typing import Tuple

def solve():
    total_count = 0
    with open('input.txt') as f:
        for line in f:
            min_count, max_count, check_char, password = parse_line(line)
            if is_password_valid(min_count, max_count, check_char, password):
                total_count += 1
    
    print(total_count)


def parse_line(input_line: str) -> Tuple[int, int, str, str]:
    line_parts = input_line.split()
    min_count = int(line_parts[0].split("-")[0])
    max_count = int(line_parts[0].split("-")[1])
    check_char = line_parts[1][0]
    password = line_parts[2]
    return min_count, max_count, check_char, password



def is_password_valid(min_count: int, max_count: int, check_char: str, password: str):
    char_count = password.count(check_char)
    return char_count >= min_count and char_count <= max_count


if __name__ == "__main__":
    solve()