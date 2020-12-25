CARD_PUBLIC_KEY_1 = 5764801
DOOR_PUBLIC_KEY_1 = 17807724

CARD_PUBLIC_KEY_2 = 11404017
DOOR_PUBLIC_KEY_2 = 13768789

SUBJECT_NUMBER = 7


def solve():

    card_public_key = CARD_PUBLIC_KEY_2
    door_public_key = DOOR_PUBLIC_KEY_2

    card_loop_size = get_loop_size(card_public_key)
    door_loop_size = get_loop_size(door_public_key)

    encryption_key1 = run_loop(card_public_key, door_loop_size)
    encryption_key2 = run_loop(door_public_key, card_loop_size)

    print(encryption_key1)
    print(encryption_key2)


def get_loop_size(public_key: int) -> int:
    number = 1
    counter = 0

    while number != public_key:
        counter += 1
        number *= SUBJECT_NUMBER
        number = number % 20201227

    print(f'counter: {counter}')
    return counter


def run_loop(public_key: int, loop_size: int):
    number = 1
    for _ in range(loop_size):
        number *= public_key
        number = number % 20201227
    
    return number


if __name__ == "__main__":
    solve()
