from copy import deepcopy


def solve():
    d = 1
    a = 1
    from_x = 0
    from_y = 0
    from_z = 0
    from_zz = 0
    w, h, cube = parse_input('input.txt')

    print(f'cube: {cube}')

    for _ in range(6):
        new_cube = deepcopy(cube)
        w += 2
        h += 2
        d += 2
        a += 2
        from_x -= 1
        from_y -= 1
        from_z -= 1
        from_zz -= 1
        for _x in range(w):
            for _y in range(h):
                for _z in range(d):
                    for _zz in range(a):
                        x = from_x + _x
                        y = from_y + _y
                        z = from_z + _z
                        zz = from_zz + _zz
                        cell = get_cell(cube, x, y, z, zz)
                        neighbours = get_neighbours(cube, x, y, z, zz)
                        active_neighbours = sum(neighbours)
                        if cell == 1 and active_neighbours not in [2, 3]:
                            set_cell(new_cube, x, y, z, zz, 0)
                        elif cell == 0 and active_neighbours == 3:
                            set_cell(new_cube, x, y, z, zz, 1)
        cube = new_cube
    
    active_cells = 0
    for _x in range(w):
        for _y in range(h):
            for _z in range(d):
                for _zz in range(a):
                    x = from_x + _x
                    y = from_y + _y
                    z = from_z + _z
                    zz = from_zz + _zz
                    active_cells += get_cell(cube, x, y, z, zz)
    
    print(active_cells)
                    

def set_cell(cube, x, y, z, zz, value):
    get_cell(cube, x, y, z, zz)
    cube[x][y][z][zz] = value
                    

def get_cell(cube, x, y, z, zz):
    if x not in cube:
        cube[x] = {}
    if y not in cube[x]:
        cube[x][y] = {}
    if z not in cube[x][y]:
        cube[x][y][z] = {}
    if zz not in cube[x][y][z]:
        cube[x][y][z][zz] = 0
    return cube[x][y][z][zz]


def get_neighbours(cube, x, y, z, zz):
    neighbours = []
    for _x in [-1, 0, 1]:
        for _y in [-1, 0, 1]:
            for _z in [-1, 0, 1]:
                for _zz in [-1, 0, 1]:
                    if _x == _y == _z == _zz == 0:
                        continue
                    neighbours.append(get_cell(cube, x + _x, y + _y, z + _z, zz + _zz))
    return neighbours
    

def parse_input(input_file: str) -> dict:
    cube = {}
    w = 0
    h = 0
    with open(input_file) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                break
            w += 1
            for j, status in enumerate(list(line)):
                h += 1
                if i not in cube:
                    cube[i] = {}
                if j not in cube[i]:
                    cube[i][j] = {}
                cube[i][j][0] = {}
                status_int = 0 if status == '.' else 1
                cube[i][j][0][0] = status_int
    return w, h, cube


if __name__ == "__main__":
    solve()