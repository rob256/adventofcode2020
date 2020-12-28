from typing import Tuple, Iterable, List, Dict


Tiles = Dict[Tuple[int, int], int]

WHITE = 0
BLACK = 1


def solve():
    x = 0
    y = 0
    moves = get_moves('input.txt')
    tiles = {}
    for move in moves:
        x, y = make_move(move, 0, 0)
        tiles[(x, y)] = abs(tiles.get((x, y), 0) - 1)
        for neighbour in get_neighbours(x, y):
            if neighbour not in tiles:
                tiles[neighbour] = 0
    
    for i in range(100):
        new_tiles = {}
        for (x, y), color in tiles.items():
            black_count = count_black_neighbours(tiles, x, y)
            if color == BLACK and (black_count == 0 or black_count > 2):
                new_tiles[(x, y)] = WHITE
            elif color == WHITE and black_count == 2:
                new_tiles[(x, y)] = BLACK
                for neighbour in get_neighbours(x, y):
                    if neighbour not in tiles:
                        new_tiles[neighbour] = WHITE
            else:
                new_tiles[(x, y)] = color
        tiles = new_tiles
        print(f'{i + 1}: {sum(tiles.values())}')
    
    print(sum(tiles.values()))


def get_moves(input_file: str) -> List[str]:
    with open(input_file) as f:
        lines = [line.strip() for line in f if line]
    return lines


def get_neighbours(x: int, y: int) -> Iterable[Tuple[int, int]]:
    x_delta = ((x + 1) % 2) * 2 - 1
    neighbour_coords = [
        (-2, 0),
        (2, 0),
        (1, 0),
        (-1, 0),
        (1, x_delta),
        (-1, x_delta),
    ]
    for _x, _y in neighbour_coords:
        yield x + _x, y + _y


def count_black_neighbours(tiles: Tiles, x: int, y: int) -> int:
    count = 0

    for _x, _y in get_neighbours(x, y):
        count += tiles.get((_x, _y), 0)

    return count


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