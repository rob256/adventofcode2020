def solve(input_file):
    total = 1
    for positions in (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ):
        trees = count_trees_on_slope(*positions, input_file=input_file)
        total *= trees
    print(total)


def count_trees_on_slope(right, down, input_file="input.txt"):
    x_pos = 0
    number_of_trees = 0
    line_number = 0
    with open(input_file) as f:
        for line in f:
            if line_number % down > 0:
                line_number += 1
                continue
            line = line.rstrip()
            line_length = len(line)
            x_pos = x_pos % line_length
            if line[x_pos] == "#":
                number_of_trees += 1
            x_pos += right
            line_number += 1
    return number_of_trees


if __name__ == "__main__":
    solve('input.txt')