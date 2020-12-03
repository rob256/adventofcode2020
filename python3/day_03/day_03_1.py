def solve(input_file):
    x_pos = 0
    number_of_trees = 0
    with open(input_file) as f:
        for line in f:
            line = line.rstrip()
            line_length = len(line)
            x_pos = x_pos % line_length
            if line[x_pos] == "#":
                number_of_trees += 1
            x_pos += 3
    print(number_of_trees)


if __name__ == "__main__":
    solve('input.txt')