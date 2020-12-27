import queue
import re
from collections import defaultdict, Counter
from typing import Dict, List


def solve():
    tiles = parse_input('input.txt')
    tiles_queue = queue.deque(list(tiles))
    edges = defaultdict(list)
    starting_tile_number = tiles_queue.popleft()
    for edge in tiles[starting_tile_number]:
        edges[edge].append(starting_tile_number)
    
    while tiles_queue:
        tile_number = tiles_queue.popleft()
        if not tile_edge_matches(tiles[tile_number], edges):
            tiles_queue.append(tile_number)
            continue
        for edge in tiles[tile_number]:
            edges[edge].append(tile_number)

    edge_tiles = []
    for tile_numbers in edges.values():
        if len(tile_numbers) == 1:
            edge_tiles.append(tile_numbers[0])

    edge_counts = Counter(edge_tiles)

    answer = 1

    for k, v in edge_counts.items():
        if v == 4:
            answer *= int(k)
            print(k)
    
    print(answer)


def parse_input(input_file: str) -> Dict[str, List[str]]:
    tiles = defaultdict(list)
    with open(input_file) as f:
        lines = [line.strip() for line in f]
    i = 0
    while i < len(lines):
        tile_number = re.findall('[0-9]+', lines[i])[0]
        edge1 = lines[i + 1]
        edge2 = lines[i + 10]
        edge3 = ''.join(lines[i + x][0] for x in range(1, 11))
        edge4 = ''.join(lines[i + x][-1] for x in range(1, 11))
        tiles[tile_number] = [edge1, edge2, edge3, edge4, ''.join(reversed(edge1)), ''.join(reversed(edge2)), ''.join(reversed(edge3)), ''.join(reversed(edge4))]
        i += 12
    return tiles
    

def tile_edge_matches(tile_edges, edges):
    for edge in tile_edges:
        if edge in edges:
            return True
    return False


if __name__ == "__main__":
    solve()