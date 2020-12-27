import queue
import re
from collections import defaultdict, Counter
from typing import Dict, List


class Tile():
    def __init__(self, tile_number, data):
        self.tile_number = tile_number
        self.data = data
        self.set_edges()

    def set_edges(self):
        self.top = self.data[0]
        self.bottom = self.data[9]
        self.left = ''.join(self.data[x][0] for x in range(10))
        self.right = ''.join(self.data[x][-1] for x in range(10))
        self.edges = [self.top, self.bottom, self.left, self.right, ''.join(reversed(self.top)), ''.join(reversed(self.bottom)), ''.join(reversed(self.left)), ''.join(reversed(self.right))]

    def rotate(self):
        new_data = []

        for j in range(10):
            row = ''
            i = 9
            while i >= 0:
                row += self.data[i][j]
                i -= 1
            new_data.append(row)
                
        
        self.data = new_data
        self.set_edges()
    
    def flip(self):
        new_data = []

        for i in range(10):
            new_data.append(''.join(reversed(self.data[i])))
        
        self.data = new_data
        self.set_edges()
    
    @property
    def content(self):
        pass

    def __repr__(self):
        return f'<Tile {self.tile_number}>'
    
    def print(self):
        for row in self.data:
            print(row)
    
                
def solve():
    tiles = parse_input('input.txt')
    print(tiles)
    tiles_queue = queue.deque(list(tiles))
    edges = defaultdict(list)
    starting_tile_number = tiles_queue.popleft()
    for edge in tiles[starting_tile_number].edges:
        edges[edge].append(tiles[starting_tile_number])
    
    while tiles_queue:
        tile_number = tiles_queue.popleft()
        if not tile_edge_matches(tiles[tile_number].edges, edges):
            tiles_queue.append(tile_number)
            continue
        for edge in tiles[tile_number].edges:
            edges[edge].append(tiles[tile_number])

    edge_tiles = []
    for _tiles in edges.values():
        if len(_tiles) == 1:
            edge_tiles.append(_tiles[0])

    edge_counts = Counter(edge_tiles)
    corner = None

    for k, v in edge_counts.items():
        if v == 4 and len(edges[k.right]) == 2 and len(edges[k.bottom]) == 2:
            corner = k
            break
    
    print(f'Top left: {corner}')

    row = [corner]
    table = [row]
    current: Tile = corner

    while True:
        if len(edges[current.right]) > 1:
            next_tile = [tile for tile in edges[current.right] if tile.tile_number != current.tile_number][0]
            count = 0
            while current.right != next_tile.left:
                if count == 5:
                    next_tile.flip()
                elif count == 10:
                    raise ValueError('bla')
                else:
                    next_tile.rotate()
                count += 1
            row.append(next_tile)
            current = next_tile
        elif len(edges[row[0].bottom]) > 1:
            current = row[0]
            next_tile = [tile for tile in edges[current.bottom] if tile.tile_number != current.tile_number][0]
            count = 0
            while current.bottom != next_tile.top:
                if count == 5:
                    next_tile.flip()
                else:
                    next_tile.rotate()
                count += 1
            row = [next_tile]
            table.append(row)
            current = next_tile
        else:
            break
    
    max_monsters = 0

    table_string = merge_tiles(table)
    print()
    print_table_string(table_string)
    print()
    max_monsters = max(max_monsters, count_sea_monsters(table_string))
    table_string = rotate_table_string(table_string)
    max_monsters = max(max_monsters, count_sea_monsters(table_string))
    table_string = rotate_table_string(table_string)
    max_monsters = max(max_monsters, count_sea_monsters(table_string))
    table_string = rotate_table_string(table_string)
    max_monsters = max(max_monsters, count_sea_monsters(table_string))
    table_string = flip_table_string(table_string)
    max_monsters = max(max_monsters, count_sea_monsters(table_string))
    table_string = rotate_table_string(table_string)
    max_monsters = max(max_monsters, count_sea_monsters(table_string))
    table_string = rotate_table_string(table_string)
    max_monsters = max(max_monsters, count_sea_monsters(table_string))
    table_string = rotate_table_string(table_string)
    max_monsters = max(max_monsters, count_sea_monsters(table_string))

    print(f'sea monsters: {max_monsters}')
    print(f'total hashes: {count_hashes(table_string)}')

    print(f'answer: {count_hashes(table_string) - (15*max_monsters)}')



def count_hashes(table_string):
    total = 0
    for row in table_string:
        total += row.count('#')
    return total

def match_1(s):
    return re.match('..................#.', s)

def match_2(s):
    return re.match('.*#....##....##....###.*', s)

def match_3(s):
    return re.match('.#..#..#..#..#..#...', s)


def count_sea_monsters(table_string):
    total = 0
    width = len(table_string)
    i = 1
    while i < width - 1:
        if match_2(table_string[i]):
            j = 0
            while j < width - 19:
                s1 = table_string[i - 1][j: j + 20]
                s2 = table_string[i][j: j + 20]
                s3 = table_string[i + 1][j: j + 20]
                if match_1(s1) and match_2(s2) and match_3(s3):
                    total += 1
                    j += 20
                else:
                    j += 1
        i += 1
    return total


def rotate_table_string(table_string):
    width = len(table_string)
    new_table = []

    for j in range(width):
        row = ''
        i = width - 1
        while i >= 0:
            row += table_string[i][j]
            i -= 1
        new_table.append(row)
    
    return new_table


def flip_table_string(table_string):
    new_table = []

    for row in table_string:
        new_table.append(''.join(reversed(row)))
    
    return new_table


def merge_tiles(table):
    new_table = []
    for row in table:
        for i in range(8):
            new_row = ''
            for tile in row:
                new_row += tile.data[i + 1][1:-1]
            new_table.append(new_row)
    return new_table
            

def print_table_string(table_string):
    for row in table_string:
        print(row)
    

def parse_input(input_file: str) -> Dict[str, List[str]]:
    tiles = {}
    with open(input_file) as f:
        lines = [line.strip() for line in f]
    i = 0
    while i < len(lines):
        tile_number = re.findall('[0-9]+', lines[i])[0]
        data = [lines[i + x] for x in range(1, 11)]
        tile = Tile(tile_number, data)
        tiles[tile_number] = tile
        i += 12
    return tiles
    

def tile_edge_matches(tile_edges, edges):
    for edge in tile_edges:
        if edge in edges:
            return True
    return False


if __name__ == "__main__":
    solve()