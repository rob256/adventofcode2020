from typing import List


SeatingPlan = List[List[int]]


def solve():
    seating_plan = get_seating_plan('input.txt')
    settled_seating_plan = get_settled_seating_plan(seating_plan)
    occupied_seats = count_occupied_seats(settled_seating_plan)
    print(occupied_seats)


def get_seating_plan(input_file: str) -> SeatingPlan:
    """
    0 = floor
    1 = empty
    2 = occupied
    """
    str_to_piece = {
        '.': 0,
        'L': 1,
        '#': 2,
    }
    seating_plan = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            seating_plan.append([str_to_piece[c] for c in line])
    return seating_plan


def get_settled_seating_plan(seating_plan: SeatingPlan) -> SeatingPlan:
    old_seating_plan = None

    while not is_same_seating_plan(seating_plan, old_seating_plan):
        old_seating_plan = seating_plan
        seating_plan = run_round(old_seating_plan)
    
    return seating_plan


def is_same_seating_plan(seating_plan1: SeatingPlan, seating_plan2: SeatingPlan) -> bool:
    if seating_plan2 is None:
        return False

    for i, _ in enumerate(seating_plan1):
        for j, _ in enumerate(seating_plan1[i]):
            if seating_plan1[i][j] != seating_plan2[i][j]:
                return False
    return True


def run_round(seating_plan: SeatingPlan) -> SeatingPlan:
    new_seating_plan = []
    for i, seating_row in enumerate(seating_plan):
        new_seating_row = []
        new_seating_plan.append(new_seating_row)
        for j, seat in enumerate(seating_row):
            adjacent_occupied_seats = get_adjacent_occupied_seats(seating_plan, i, j)
            if seat == 1 and adjacent_occupied_seats == 0:
                new_seating_row.append(2)
            elif seat == 2 and adjacent_occupied_seats >= 4:
                new_seating_row.append(1)
            else:
                new_seating_row.append(seat)
    return new_seating_plan
        

def get_adjacent_occupied_seats(seating_plan: SeatingPlan, i: int, j: int) -> int:
    total = 0
    for _i in [-1, 0, 1]:
        for _j in [-1, 0, 1]:
            if _i == 0 and _j == 0:
                continue
            if i + _i < 0:
                continue
            if j + _j < 0:
                continue
            try:
                if seating_plan[i + _i][j + _j] == 2:
                    total += 1
            except IndexError:
                pass
    return total


def count_occupied_seats(seating_plan: SeatingPlan) -> int:
    total = 0
    for seating_row in seating_plan:
        for seat in seating_row:
            if seat == 2:
                total += 1
    return total


if __name__ == "__main__":
    solve()