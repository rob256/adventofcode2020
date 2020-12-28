from typing import Tuple, Iterable, List


def solve():
    x = 0
    y = 0
    moves = get_moves('input.txt')
    tiles = {}
    for move in moves:
        x, y = make_move(move, 0, 0)
        tiles[(x, y)] = abs(tiles.get((x, y), 0) - 1)

    print(sum(tiles.values()))


def get_moves(input_file: str) -> List[str]:
    with open(input_file) as f:
        lines = [line.strip() for line in f if line]
    return lines


def make_move(move: str, x: int, y: int) -> Tuple[int, int]:
    for m in split_move(move):
        if m == 'e':
            x += 2
        elif m == 'w':
            x -= 2
        elif m == 'ne':
            y_delta = (x + 1) % 2
            x += 1
            y += y_delta
        elif m == 'se':
            y_delta = x % 2
            x += 1
            y -= y_delta
        elif m == 'nw':
            y_delta = (x + 1) % 2
            x -= 1
            y += y_delta
        elif m == 'sw':
            y_delta = x % 2
            x -= 1
            y -= y_delta
    return x, y


def split_move(move: str) -> Iterable[str]:
    i = 0
    while i < len(move):
        if move[i] in ['n', 's']:
            yield move[i: i + 2]
            i += 2
        else:
            yield move[i]
            i += 1
        

if __name__ == "__main__":
    solve()