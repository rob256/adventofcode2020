def solve():

    max_seat_id = 0

    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            seat_id = get_seat_id(line)
            max_seat_id = max(max_seat_id, get_seat_id(line))
    print(max_seat_id)



def get_seat_id(seat_str: str) -> int:
    current_min_long = 0
    current_max_long = 127
    current_min_short = 0
    current_max_short = 7
    for seat_char in seat_str:
        long_range_half = (current_max_long - current_min_long + 1) / 2
        min_range_half = (current_max_short - current_min_short + 1) / 2
        if seat_char == "F":
            current_max_long -= long_range_half
        if seat_char == "B":
            current_min_long += long_range_half
        if seat_char == "L":
            current_max_short -= min_range_half
        if seat_char == "R":
            current_min_short += min_range_half
    return int(current_min_long * 8 + current_min_short)


if __name__ == "__main__":
    solve()