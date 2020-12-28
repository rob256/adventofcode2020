from typing import Tuple, List


class Cup:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f'<Cup value={self.value}>'


def solve():

    def get_target():
        current_value = current.value
        target_value = current_value - 1 if current_value > 1 else max(puzzle_input)
        while target_value in taken:
            target_value = target_value - 1 if target_value > 1 else max(puzzle_input)
        return num_to_cup[target_value]

    puzzle_input = list(map(int, "315679824"))
    start = Cup(int(puzzle_input[0]))

    num_to_cup = {
        puzzle_input[0]: start,
    }

    current = start
    for n in puzzle_input[1:]:
        cup = Cup(n)
        current.next = cup
        current = cup
        num_to_cup[n] = current
    
    print(num_to_cup)
    
    current.next = start

    current = start

    for _ in range(100):
        cup_3, taken = take_3(current)
        target = get_target()
        place_3(cup_3, target)
        current = current.next
    
    current = num_to_cup[1]
    current = current.next
    order = []
    while current.value != 1:
        order.append(current.value)
        current = current.next
    
    print(''.join(str(x) for x in order))
    



def take_3(cup: Cup) -> Tuple[Cup, List[int]]:
    cup_3 = cup.next
    cup.next = cup_3.next.next.next
    cup_3.next.next.next = None
    print(cup_3)
    print(cup_3.next)
    print(cup_3.next.next)

    return cup_3, [cup_3.value, cup_3.next.value, cup_3.next.next.value]


def place_3(cup_3: Cup, after: Cup):
    after_next = after.next
    after.next = cup_3
    cup_3.next.next.next = after_next


if __name__ == "__main__":
    solve()